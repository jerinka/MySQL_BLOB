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


sql = "INSERT INTO customers (name, addess) VALUES (%s, %s)"
val = ("Tom", "Highway 22")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")



