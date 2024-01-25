#sqlite.py

import sqlite3 as sq

#연결객체
# con = sq.connect ("c:\\work\\test.db")
con = sq.connect (":memory:")

#커서
cur = con.cursor()
#테이블을 생성
cur.execute("create table PhoneBook (name text, phoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values ('김길동', '010-222');")

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

