import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="hospital"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE daktari (FIRST_NAME VARCHAR(255), LAST_NAMEVARCHAR(255), AGE INT(3) , GENDER VARCHAR(8), SPECIALITY VARCHAR(255),INCOME decimal(15,2))")


#establishing the connection
conn = mysql.connector.connect(
   user='root', password='yourpassword', host='127.0.0.1', database='hospital')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO daktari(
   FIRST_NAME, LAST_NAME, AGE, GENDER, SPECIALITY,INCOME)
   VALUES ('Coronasias', 'Onyango', 40, 'MLAE', 80000)"""

try:
   # Executing the SQL command
   cursor.execute(sql)

   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

# Closing the connection
conn.close()