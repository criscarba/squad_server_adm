import pandas as pd
from datetime import datetime
import shutil

server_config_root_dir = 'C:\squad_server\SquadGame\ServerConfig'
bkp_root_dir = 'bkp'


def build_sheet_url(doc_id):
    return f'https://docs.google.com/spreadsheets/d/{doc_id}/export?gid=0&format=csv'

def filter_db(df, Role):
    admin_role_mask = df['Role'] == Role
    return df[admin_role_mask]

def get_line(Name, SteamID, Role, DateFrom, DateTO):
    if Role == "SuperAdmin":
        return f"\n//{Name}\nAdmin={SteamID}:{Role}\n"
    else:    
        return f"\n//{Name} - Desde: {DateFrom} - Hasta: {DateTO}\nAdmin={SteamID}:{Role}\n"
    
def create_admin_cfg_file():
    DOC_ID = '1iqwjl8X6Eb_VgXFiKmzZT8d8NzCiFwhGfnRwacxuSZw'    

    sheet_url = build_sheet_url(DOC_ID)
    db_admins_and_users = pd.read_csv(sheet_url)
    db_admins_and_users['SteamID'] = db_admins_and_users.apply(lambda x: str(int(x['SteamID'])), axis=1)

    header_file = open(f"Header.txt", "r")
    header = header_file.readlines()
    
    admin_file = open("Admins.cfg", "w")
    for line in header:
        admin_file.write(str(line))
    
    hg_admins_header = """

    // ++++++++++++++++++++++++++++++++++ // 
    // ++++++++ HG SERVER ADMINS ++++++++ //
    // ++++++++++++++++++++++++++++++++++ //

    """
    admin_file.write(str(hg_admins_header))
    hg_admins = filter_db(db_admins_and_users, 'SuperAdmin')
    for index, row in hg_admins.iterrows():
        if row['Excluded'] != "x":
            admin_file.write(get_line(row['Name'], 
                                    row['SteamID'],
                                    row['Role'],
                                    row['DateFrom'],
                                    row['DateTo']))
    
    hg_vips_header = """

    // ++++++++++++++++++++++++++++++++++ // 
    // ++++++++++++ VIP LIST ++++++++++++ //
    // ++++++++++++++++++++++++++++++++++ //

    """
    admin_file.write(str(hg_vips_header))

    hg_vips = filter_db(db_admins_and_users, 'Vip')
    for index, row in hg_vips.iterrows():
        if row['Excluded'] != "x":
            current_date = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 0, 0)
            if current_date <= datetime.strptime(row['DateTo'],"%d/%m/%y"):
                admin_file.write(get_line(row['Name'], 
                                        row['SteamID'],
                                        row['Role'],
                                        row['DateFrom'],
                                        row['DateTo']))
    admin_file.close()

def bkp_old_admin_cfg_file():
    shutil.copy2(f'{server_config_root_dir}/Admins.cfg', f'bkp/BKP-{datetime.now().strftime("%Y%m%dT%H:%M:%S")}-Admins.cfg')
    
def move_new_admin_cfg_file():
    shutil.move(f'Admins.cfg', f'{server_config_root_dir}/Admins.cfg')
    
def main():    
    create_admin_cfg_file()          
    
        
if __name__ == "__main__":
    main()