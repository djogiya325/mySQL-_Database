import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='@Python08', host='127.0.0.1', database='MuleSoft')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving the list of tables
print("List of tables in the database: ")
cursor.execute("SHOW Tables")
print(cursor.fetchall())

#Doping EMPLOYEE table if already exists
cursor.execute("DROP TABLE IF EXISTS MOVIES")
print("Table dropped... ")

#Retrieving the list of tables
print("List of tables after dropping the MOVIES table: ")
cursor.execute("SHOW Tables")
print(cursor.fetchall())

#Closing the connection
conn.close()