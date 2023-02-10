#bin/bash/python3

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
)

mycursor=mydb.cursor()

mycursor.execute("CREATE DATABASE hospital")

for exist in mycursor:
    print(exist)