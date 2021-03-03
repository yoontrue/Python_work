import sqlite3

conn = sqlite3.connect('test.db')
sql = """update saram set name=?, age=? where id=?"""

update_data = [
    ('yusin',35,'shin'),
    ('yusin2',36,'kang'),
    ('yusin3',37,'lee')
]

c = conn.cursor()
c.executemany(sql, update_data)

c.close()

conn.commit()
conn.close()