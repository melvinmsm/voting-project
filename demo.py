import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="")

mycursor=mydb.cursor()
mycursor.execute("use sakila")
mycursor.execute("show tables")


for i in mycursor:
    print(i)