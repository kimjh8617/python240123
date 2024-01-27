#연습01.py

class Person:
    def __init__(self): #초기화 메서드
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

p1 = Person()
p2 = Person()
p1.name = "전우치"
p1.print()
p2.print()

#런타임시에 title 변수 추가
Person.title = "New title"
print(p1.title)
print(p2.title)
print(Person.title)