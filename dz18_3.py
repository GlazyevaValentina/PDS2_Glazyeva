import mysql.connector

# Create Connection to Database
mydb_exp = mysql.connector.connect(
    host="localhost",
    user="root",
    password="070809Luda",
    database="my_second_db"
)

# Creating one more Table
mycursor = mydb_exp.cursor()
mycursor.execute("CREATE TABLE employee (ID INT AUTO_INCREMENT KEY, name VARCHAR(255), salary INT(6))")

# Check if Table Exists
mydb_exp = mysql.connector.connect(
    host="localhost",
    user="root",
    password="070809Luda",
    database="my_second_db"
)

mycursor = mydb_exp.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
