import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user='jerin',
    password='jerin123',
    database='ml_database'
    )

mycursor =mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

