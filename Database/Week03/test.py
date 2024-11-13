import mysql.connector
db = "python_db"
mydb= mysql.connector.Connect(host='localhost',user='root',passwd='password',database=db)

mycursor = mydb.cursor()

query1 = """ CREATE TABLE student(
            id int primary key auto_increment,
            name varchar(250),
            roll int (10)
        )"""

query2 = """ INSERT INTO student(id,roll,name) VALUES(1,101,'shoyeb')"""
query3 = """ UPDATE student SET(id,roll,name) VALUES(1,101,'shoyeb')"""

mycursor.execute(query)
mydb.commit()


