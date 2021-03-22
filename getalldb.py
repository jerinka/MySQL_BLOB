import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="jerin",
  password="jerin123"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute('CREATE DATABASE ml_database')


