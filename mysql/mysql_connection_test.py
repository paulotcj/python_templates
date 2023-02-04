import mysql.connector

print("testing mysql")

server_address = "localhost"
database_name = "python_database"

mydb = mysql.connector.connect(
  host=server_address,
  user="xxxxxxxxxx",
  password="xxxxxxxxxx"
)

print("Connection successful? ->",mydb)


