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
#입력 파라메터 처리
name = "전우치"
phoneNum = ("010-123")
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNum))
#여러개 행을 입력
datalist = (("이순신", "010-444"), 
            ("김제형", "019-002"),
            ("김우빈", "019-537"),
            ("조현배", "019-567"),
            ("박상훈", "019-577"),
            ("김민수", "019-597"),
            ("차준향", "019-517"),
            ("이정제", "019-527"),
            ("박문수", "019-001"))
cur.executemany("insert into PhoneBook values (?, ?);", (datalist))


#검색
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)

print("----fetchone()----")
print(cur.fetchone())
print("----fetchmant(3)----")
print(cur.fetchmany(3))
print("----fetchall()----")
print(cur.fetchall())
cur.exxcute("select")
