class Person:
    def __init__(self, person_id, name):
        self.id = person_id
        self.name = name

    def printinfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, person_id, name, title):
        super().__init__(person_id, name)
        self.title = title

    def printinfo(self):
        super().printinfo()
        print(f"Title: {self.title}")

class Employee(Person):
    def __init__(self, person_id, name, skill):
        super().__init__(person_id, name)
        self.skill = skill

    def printinfo(self):
        super().printinfo()
        print(f"Skill: {self.skill}")

# 샘플 코드
person1 = Person(1, "John")
person1.printinfo()

manager1 = Manager(2, "Alice", "Project Manager")
manager1.printinfo()

employee1 = Employee(3, "Bob", "Python, Java, C++")
employee1.printinfo()
