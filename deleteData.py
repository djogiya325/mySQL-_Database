import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='@Python08', host='127.0.0.1', database='MuleSoft')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving single row
print("Contents of the table: ")
cursor.execute("SELECT * from MOVIES")
print(cursor.fetchall())

#Preparing the query to delete records
sql = "DELETE FROM MOVIES WHERE YEAR_OF_RELEASE > '%d'" % (2014)

try:
   # Execute the SQL command
   cursor.execute(sql)
   
   # Commit your changes in the database
   conn.commit()
except:
   # Roll back in case there is any error
   conn.rollback()

#Retrieving data
print("Contents of the table after delete operation ")
cursor.execute("SELECT * from MOVIES")
print(cursor.fetchall())

#Closing the connection
conn.close()