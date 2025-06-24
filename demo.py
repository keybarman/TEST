import mysql.connector
cnx=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="world",
    user="root",
    password="abcABC123")


print("透過連線取得cursor物件")
dbcursor=cnx.cursor()
print("執行 select name from city")
dbcursor.execute("select name from city")
