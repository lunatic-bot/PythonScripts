import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "SqlPython771#",
        database = "testdb"
)

# print(mydb)
## creating a cursor object
# mycursor = mydb.cursor()

## Execute the command
# mycursor.execute("CREATE DATABASE TESTDB")

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)


## creating tables
# creating a cursor object
mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
# mycursor.execute("SHOW TABLES")

# for tb in mycursor:
#     print(tb)


InputFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# student1 = ("Arpit", 24)
students = [("Arpit", 24), ("Ankit", 18), 
            ("Shlok", 12), ("Amanda", 21), 
            ("Rachel", 24), ("Bob", 17)]

## for one entry
# mycursor.execute(InputFormula, student1)

## for many entries
# mycursor.executemany(InputFormula, students)
# mydb.commit()


# mycursor.execute("SELECT name from students")
## fetch all the result from last executed statement
# myresult = mycursor.fetchall()

## fetch one entry from last executed statement
# myresult = mycursor.fetchone()



# sql = "SELECT * FROM students WHERE name = 'Arpit'"

## wildcard characters
# use like ->> % - one or more occurance, _ - exactly one occurance
# sql = "SELECT * FROM students WHERE name LIKE 'A%'"
# sql = "SELECT * FROM students WHERE name = %s"




# # mycursor.execute(sql)
# mycursor.execute(sql, ('Arpit', ))

# myresult = mycursor.fetchall()

# for row in myresult:
#     print(row)



## Updation ::

# sql = "UPDATE students SET age = 15 WHERE name = 'Bob'"
# mydb.commit()

## limiting values to be displayed
# mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 2")

# myresult = mycursor.fetchall()

# for val in myresult:
#     print(val)



# ## Order by ::

# sql = "SELECT * FROM students ORDER BY name DESC"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()
# for val in myresult:
#     print(val)


## Delete ::


# ## Order by ::

# sql = "DELETE FROM students WHERE name = 'Arpit'"

# mycursor.execute(sql)
# mydb.commit()


## delete table
sql = "DROP TABLE IF EXISTS students"



