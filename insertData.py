import mysql.connector

#establishing the connection

conn = mysql.connector.connect(user='root', password='@Python08', host='127.0.0.1', database='MuleSoft')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO MOVIES(
   NAME, ACTOR_NAME, ACTRESS_NAME, DIRECTOR_NAME, YEAR_OF_RELEASE)
   VALUES ('Veer', 'Salman Khan', 'Zareen Khan', 'Anil Sharma', 2010),
   ('Bhuj','Ajay Devagan','Sonakshi Sinha','Abhishek Dudhaiya',2021),
   ('PK','Aamir Khan','Anushka Sharma','Rajkumar Hirani',2014),
   ('Raees','Shah Rukh Khan','Mahira Khan','Rahul Dholakia',2017)
   """

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