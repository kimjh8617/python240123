# classpractice.py
# 1. 클래스를 정의

class Person:
    #초기화 메서드
    def __init__(self): # self는 인스턴스 자신을 가리킴
        #인스터스 멤버변수
        self.name = "홍길동"
    def print(self):
        print("내 이름은 {0}".format(self.name))
# 2. 인스턴스 생성

p1 = Person()
p2 = Person()
p1. name = "전우치"

# 3. 메서드 호출
p1.print()
p2.print()



# # 전역변수
# strName = "전역변수의 값"

# class Demo:
#     def __init__(self):
#         self.strname()




#실행시간에 변수 추가

Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

