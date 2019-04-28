import sqlite3
db=sqlite3.connect('/home/rajendran/Documents/test')
#sql="SELECT * from student;"
sql="SELECT * from user;"
cur=db.cursor()
try:
    cur.execute(sql)
except Exception as e:
    e.mes
else:
    pass
finally:
    pass


while True:
    record=cur.fetchone()
    if record==None:
        break
    print (record)
db.close()
