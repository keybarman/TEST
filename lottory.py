import mysql.connector
cnx=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="prize",
    user="root",
    password="abcABC123")
dbcursor=cnx.cursor()

insertSQL="insert into biglottory(num,n1,n2,n3,n4,n5,n6,sp) values(%s,%s,%s,%s,%s,%s,%s,%s)"
parserdata=(114062,6,20,21,31,32,33,6)
dbcursor.execute(insertSQL,parserdata)
print("寫入成功")
cnx.commit()

dbcursor.close()
cnx.close()

