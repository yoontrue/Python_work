import sqlite3
conn = sqlite3.connect('test.db')
sql = '''
insert into saram(id,name,age) values(?,?,?)
'''
person = ('lee','sunshin',21)
c = conn.cursor()
c.execute(sql, person)
c.close()

# 입력, 수정, 삭제 기능은 commit
conn.commit()
conn.close()