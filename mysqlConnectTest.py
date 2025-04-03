import mysql.connector

config = {
    'user': 'root',
    'password': '20020613',
    'host': '127.0.0.1',
    'database': 'test02',
    'raise_on_warnings': True
}

con = mysql.connector.connect(**config)

cursor = con.cursor()

cursor.execute("select * from tb_order")

for obj in cursor:
    print(f"{obj}\n")

cursor.close()
con.close()