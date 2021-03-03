import sqlite3
conn = sqlite3.connect('test.db')
sql = '''
insert into saram(id,name,age) values(?,?,?)
'''

data = [
    ('lee','sunshin',21),
    ('sho','gildong',31),
    ('shin','dolseok',25),
    ('kang','gamchan',27)
]

c = conn.cursor()
c.executemany(sql, data)
c.close()

# 입력, 수정, 삭제 기능은 commit
conn.commit()
conn.close()