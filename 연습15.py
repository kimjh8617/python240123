import sqlite3

#연결객체 생성(임시로 메모리에 저장)
con = sqlite3.connect(":memory:")
#SQL 구문을 실행할 커서 객체 리턴
cur = con.cursor()

#SQL 구문을 실행할 커서 객체 리턴
cur = con.cursor()
cur.execute(
    "create table if not exists PhoneBook" + 
    "(id integer primary key autoincrement, neme text, phoneNum text);")

cur.execute("insert into PhoneBook (name, phoneNum) values ('홍길동', '010-222-1234');")

neme = "이순신"
phoneNumber = "010-222-1234"
cur.execute("insert into PhoneBook (name, phoneNum) values (?, ?;)",
             (name, phoneNumber))

datalist = (("전우치", "010-123-1234"), ("박문수", "010-1234-5678"))
cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);",
                datalist)
            
cur.execute("selcet * from PhoneBook;")
for row in cur:
    print(row)
