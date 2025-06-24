import mysql.connector
cnx=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="world",
    user="abc123456",
    password="abcABC123")

print("透過連線取得 cursor物件")
dbcursor=cnx.cursor()
print("執行 select name from city")
# 否則就要  select * from database.table 
print("記得開權限")
#grant insert,update,select on world.* to 'dbuser'@"%";
#flush privileges;
dbcursor.execute("select name from city")
for cityname in dbcursor:
    print(cityname)

dbcursor.execute("select name, population from country")
for (c , p ) in dbcursor:
    print(c, p)