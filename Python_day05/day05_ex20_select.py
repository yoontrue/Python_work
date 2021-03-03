import sqlite3

conn = sqlite3.connect('test.db')
sql = '''select * from saram order by name desc'''

c = conn.cursor()
c.execute(sql)

# print(c.fetchone())

# for s in c.fetchmany(3) :
#     print(s)

lis = c.fetchall()
print(type(lis))

c.execute(sql)

for s in c.fetchall() :
    print(type(s))
    print(s)

c.close()
conn.close()