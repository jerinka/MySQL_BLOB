import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='jerin',
    password='jerin123',
    database='ml_database'
    )

mycursor = mydb.cursor()

mycursor.execute("SHOW columns FROM customers")
print ([column[0] for column in mycursor.fetchall()])



mycursor.execute('SELECT * FROM customers')

myresult = mycursor.fetchall()

print('All coloumns of customers')
for x in myresult:
    print(x)

print('\nSelect coloumns of customers')

mycursor.execute("SELECT name FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
