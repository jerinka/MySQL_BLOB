import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="jerin",
  password="jerin123",
  database="mydatabase"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#mycursor.execute("ALTER TABLE customers ADD COLUMN fav INT")

'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [("John", "Highway 21"),("Tom", "Highway 30")]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


sql = "UPDATE customers SET fav = '1' WHERE name = 'Tom'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
'''


mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)









