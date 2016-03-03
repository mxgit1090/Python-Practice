import MySQLdb

# 1. Get the connection of mysql
db = MySQLdb.connect(host="localhost", port=3306, user="user", passwd="password", dbname="Database", charset="utf8")

# 2. Use the query to get the rows:
rows_first = db.query("SELECT * FROM Test WHERE name LIKE '%cat%'")

for row in rows_first.store_result():
  print row
  
# 3. Use cursor to fetch the rows:
c = db.cursor();
c.execute("SELECT * FROM Test WHERE name = %s", ("doge"))

for row in c.fetchall():
  print row
  
