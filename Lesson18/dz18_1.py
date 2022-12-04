import mysql.connector

# Creating a Database
mydb_exp = mysql.connector.connect(
    host="localhost",
    user="root",
    password="070809Luda"
)
print(mydb_exp)

mycursor = mydb_exp.cursor()
mycursor.execute("CREATE DATABASE my_second_db")

# Check if Database Exists
mydb_exp = mysql.connector.connect(
    host="localhost",
    user="root",
    password="070809Luda"
)

mycursor = mydb_exp.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
