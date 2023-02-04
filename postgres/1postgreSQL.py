import psycopg2

database_name       = "postgres"
server_address_db   = 'xxxxxx'
user_db             = "xxxxxx"
password_db         = "xxxxxx"
port_db             = "5432"
new_database        = "xxxxxx"

def test_DB_Connection():
    conn = psycopg2.connect( database=database_name, user=user_db, password=password_db, host=server_address_db, port=port_db  )
    cursor = conn.cursor()
    cursor.execute("select version()")
    data = cursor.fetchall()
    print("Connection established to: ",data)
    conn.close()

def drop_db():
    conn = psycopg2.connect( database=database_name, user=user_db, password=password_db, host=server_address_db, port=port_db  )
    conn.autocommit = True

    with conn.cursor() as cur:
        cur.execute(f"DROP DATABASE IF EXISTS {new_database};")

    conn.close()

def create_db():
    conn = psycopg2.connect( database=database_name, user=user_db, password=password_db, host=server_address_db, port=port_db  )
    conn.autocommit = True

    with conn.cursor() as cur:
        cur.execute(f"CREATE DATABASE {new_database};") 

    conn.close()               

# ------------------------------------------    
# house keeping
# test_DB_Connection()

drop_db()
create_db()

database_name = new_database

# ------------------------------------------    

conn = psycopg2.connect( database=database_name, user=user_db, password=password_db, host=server_address_db, port=port_db  )
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME text NOT NULL,
   LAST_NAME text,
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''

cursor.execute(sql)

conn.commit()

# Preparing SQL queries to INSERT a record into the database.
cursor.execute("INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Jane' , 'Doe'    , 27, 'F', 90000 )")
cursor.execute("INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('John' , 'Doe'    , 20, 'M', 90000 )")
cursor.execute("INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Mike' , 'Carr'   , 25, 'M', 83000 )")
cursor.execute("INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Stan' , 'Penrose', 26, 'F', 100000)")
cursor.execute("INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Kim'  , 'Kimura' , 24, 'F', 60000 )")

# Commit your changes in the database
conn.commit()


cursor.execute("SELECT * from EMPLOYEE")
result = cursor.fetchall();
# print(result)

for x in result:
  print(f"    {x}")

# Closing the connection
conn.close()






