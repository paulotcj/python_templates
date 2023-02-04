import mysql.connector

print("testing mysql")

server_address = "localhost"
database_name = "python_database"

mydb = mysql.connector.connect(
  host=server_address,
  user="xxxxxxxxxx",
  password="xxxxxxxxxx",
  database=database_name
)
print("--------------------------------")
print("Connection successful? ->",mydb)


mycursor = mydb.cursor()


print("--------------------------------")
print("drop database")
mycursor.execute(f"DROP DATABASE IF EXISTS {database_name}")

print("--------------------------------")
print("create database")
mycursor.execute(f"CREATE DATABASE {database_name}")

print("--------------------------------")
print("use database")
mycursor.execute(f"USE {database_name}")

print("--------------------------------")
print("SHOW DATABASES")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

print("--------------------------------")
print("create table")
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")  

print("--------------------------------")
print("SHOW TABLES")
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


print("--------------------------------")  
print("drop and create table")
mycursor.execute("DROP TABLE IF EXISTS customers")
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")  

print("--------------------------------")  
print("alter table")
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")



print("--------------------------------")  
print("insert")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


print("--------------------------------")  
print("insert multiple rows")

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


print("--------------------------------")  
print("get last rowID")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)


print("--------------------------------")  
print("SELECT FROM DB")
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(f"    {x}")



print("--------------------------------")  
print("SELECT COLUMNS")
mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)  


print("--------------------------------")  
print("FETCH ONE")
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)  
mycursor.reset()


print("--------------------------------")  
print("SELECT WITH WHERE")
sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



print("--------------------------------")  
print("preventing SQL injection by using %s")

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



print("--------------------------------")  
print("DELETE")
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")  


print("--------------------------------")  
print("DELETE WITH SQL INJECTION PRECAUTIONS")
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

print("--------------------------------")  
print("UPDATE")
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")


print("--------------------------------")  
print("UPDATE WITH SQL INJECTION PRECAUTIONS")
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()


print("--------------------------------")
print("SELECT WITH LIMIT")
mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


print("--------------------------------")
print("SELECT WITH LIMIT OF 5 AND OFFSET BY 2")
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)  

print(mycursor.rowcount, "record(s) affected")


mycursor.close()