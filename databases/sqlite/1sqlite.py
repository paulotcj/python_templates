import sqlite3
print("--------------------------------")
print("connect to the database")
con = sqlite3.connect("dbtest.db")
cur = con.cursor()

print("--------------------------------")
print("drop table if exists")
cur.execute("DROP TABLE IF EXISTS movie")

print("--------------------------------")
print("create table")
cur.execute("CREATE TABLE movie(title, year, score)")


print("--------------------------------")
print("select table names in the database")
res = cur.execute("SELECT name FROM sqlite_master")
result = res.fetchall()

for x in result:
  print(f"    {x}")

print("--------------------------------")
print("insert into table")
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
    """)  
con.commit()

print("--------------------------------")
print("select from table")
res = cur.execute("SELECT score FROM movie")

result = res.fetchall()

for x in result:
  print(f"    {x}")