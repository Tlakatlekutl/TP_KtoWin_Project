# coding: utf-8
import MySQLdb


db = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='root',
    db='ktowin_db')
c = db.cursor()
c.execute("SHOW TABLES")
c.fetchall()

c.execute("SELECT username, is_staff FROM auth_user")
c.fetchall()
