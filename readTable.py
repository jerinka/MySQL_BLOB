import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user='jerin',
    password='jerin123',
    database='ml_database'
    )

mycursor = mydb.cursor()

mycursor.execute('SHOW TABLES')

for x in mycursor:
    print(x)
