import mysql.connector

# Create Connection to Database
mydb_exp = mysql.connector.connect(
    host="localhost",
    user="root",
    password="070809Luda",
    database="my_second_db"
)

# Insert Into Table student
mycursor = mydb_exp.cursor()
sql = "INSERT INTO student (ID, name) VALUES (%s, %s)"
val = (1, "John")
mycursor.execute(sql, val)

mydb_exp.commit()
print(mycursor.rowcount, "record inserted.")

# Insert Into Table employee
mycursor = mydb_exp.cursor()
sql = "INSERT INTO employee (ID, name, salary) VALUES (%s, %s, %s)"
val = (1, "John", 100000)
mycursor.execute(sql, val)

mydb_exp.commit()
print(mycursor.rowcount, "record inserted.")
