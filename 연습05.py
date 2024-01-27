#연습05.py

#부모 클래스 정의
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone :{1})".format(self.name , self.phoneNumber))
    def working(self):
        print("지금 일하고 있음")
    def sleep(self):
        print("지금 잠자고 있음")

#자식 클래스 정의 
class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        # 부모의 생성자 메서드 호출
        Person.__init__(self, name, phoneNumber)
        
        self.subject = subject
        self.studentID = studentID

    def printInfo(self):
        print("Info(Name:{0}, Phone Number:{1})".format(self.name, self.phoneNumber))
        print("Info(subject:{0}, studentID:{1})".format(self.subject, self.studentID))


#인스턴스 생성
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "2304123")
# print(p.__dict__)
# print(s.__dict__)

s.printInfo()
s.working()
s.sleep()

        