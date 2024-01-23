class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

    def working(self):
        print("현재 작업중")

    def sleeping(self):
        print("현재 휴식중")
        
class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        # 명시적으로 부모 초기화 메서드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받고 덮어쓰기
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        print("Info(학과:{0}, 학번: {1})".format(self.name, self.phoneNumber))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "991122")

p.printInfo()
s.printInfo()
s.working()
s.sleeping()







