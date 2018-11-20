import pyodbc

server = 'server_name'
database = 'my_database'
# username = 'my_username'
# password = 'my_password'

#cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';Trusted_Connection='+'yes;')

cursor = cnxn.cursor()

cursor.execute("SELECT 4")
for row in cursor.fetchall():
    print(row)

print("DONE")
