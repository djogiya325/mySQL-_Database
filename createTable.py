import mysql.connector

#establishing the connection
    
conn = mysql.connector.connect(user='root', password='@Python08', host='127.0.0.1', database='MuleSoft')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS MOVIES")

#Creating table as per requirement
sql ='''CREATE TABLE MOVIES(
   NAME CHAR(20) NOT NULL,
   ACTOR_NAME CHAR(20),
   ACTRESS_NAME CHAR(20),
   DIRECTOR_NAME CHAR(20),
   YEAR_OF_RELEASE INT
)'''
cursor.execute(sql)

#Closing the connection
conn.close()