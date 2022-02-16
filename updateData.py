import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='@Python08', host='127.0.0.1', database='MuleSoft')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing the query to update the records
sql = '''UPDATE MOVIES SET ACTRESS_NAME = "Nora Fatehi" WHERE ACTRESS_NAME = 'Sonakshi Sinha' '''
try:
   # Execute the SQL command
   cursor.execute(sql)
   
   # Commit your changes in the database
   conn.commit()
except:
   # Rollback in case there is any error
   conn.rollback()
   
#Retrieving data
sql = '''SELECT * from MOVIES'''

#Executing the query
cursor.execute(sql)

#Displaying the result
print(cursor.fetchall())

#Closing the connection
conn.close()