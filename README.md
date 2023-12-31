# 1. Modificar dentro del archivo *Header.txt* los grupos que se tengan definidos, como por ej:

Group=Admin:kick,ban,changemap,config,manageserver,canseeadminchat
Group=Moderator:kick,ban
Group=SuperAdmin:startvote,changemap,pause,cheat,private,balance,chat,kick,ban,config,cameraman,immune,manageserver,featuretest,reserve,demos,clientdemos,debug,teamchange,forceteamchange,canseeadminchat
Group=Vip:reserve

# 2. Crear planilla en cuenta de Drive (Google Docs) con la estructura del archivo *admins_and_vips_db.xlsx*

La planilla contiene la siguiente estructura: 

Excluded => Flag que se activa con una *"x"* y sirve como bypass del criterio de fechaa *DateFrom* & *DateTo*
Name => Nombre del player
SteamID => SteamID del player
Role => El Rol que hayan definido en el archivo *Header.txt*
DateFrom => Fecha en formato tal cual viene seteado en el campo desde que abonó el VIP
DateTo => Fecha en formato tal cual viene seteado en el campo hasta que abonó el VIP
PayMethod => Campo arbitrario, a modo de control interno. 

# 3. Generar Link de Share de planilla en Drive para que genere el link de export y pueda ser consumida por el script de Python. 

El Link de export tiene la siguiente URL *'https://docs.google.com/spreadsheets/d/{doc_id}/export?gid=0&format=csv'* donde *"doc_id"* se corresponde al ID de su planilla exportada.

Es valor debe ser seteado dentro del Script en la linea 23 ==> *DOC_ID = 'xxxxxx'*


# 4. Dentro del Script de python en la linea 5, modificar la URI de donde se encuentra el archivo de Admins en su servidor Como por EJ: server_config_root_dir = 'C:\squad_server\SquadGame\ServerConfig'

# 5. Para ejecutar el script simplemente realizar "python hgadmins.py"