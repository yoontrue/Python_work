import sqlite3

conn = sqlite3.connect('test.db')
sql = """delete from saram where id='{0}'"""

del_name = 'sho'

c = conn.cursor()
c.execute(sql.format(del_name))

c.close()

conn.commit()
conn.close()