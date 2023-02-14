#bin/bash/python3

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="Wandeto",
    password="Pass123",
    database="hospital"
)

mycursor=mydb.cursor()

mycursor.execute("CREATE DATABASE hospital")

mycursor.execute("CREATE TABLE doctor (name VARCHAR(255), speciality VARCHAR(255))")

mycursor.execute("CREATE TABLE nurse (name VARCHAR(255), department VARCHAR(255))")

mycursor.execute("CREATE TABLE nurseassistant (name VARCHAR(255), age int(3), department VARCHAR(255))")

for exist in mycursor:
    print(exist)