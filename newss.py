# coding: utf-8
import MySQLdb
db = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='root',
    db='ktowin_db')
c = db.cursor()
c.execute("SELECT (%s, %s) FROM auth_user", ("username", "is_staff"
))
c.execute("SELECT (%s), (%s) FROM auth_user", ("username", "is_staff"))
c.fetchall()
c.execute("SELECT (%s), (%s) FROM auth_user", "username", "is_staff")
c.execute("SELECT (%s), (%s) FROM auth_user", ("username", "is_staff"))
c.execute("SELECT (%s) FROM auth_user", ("username", "is_staff"))
c.execute("SELECT (%s), (%s) FROM auth_user", ("username", "is_staff"))
c.fetchall()
c.execute("SELECT username, is_staff FROM auth_user")
c.fetchall()
