import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='@Python08', host='127.0.0.1', database='MuleSoft')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving single row
sql = '''SELECT * from MOVIES LIMIT 2'''

#Executing the query
cursor.execute(sql)

#Fetching the data
result = cursor.fetchall();
print(result)

#Closing the connection
conn.close()