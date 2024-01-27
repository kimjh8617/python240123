#연습02.py

strName = "전역변수의 값"

class Demostring:
    def __init__(self):
        self.strName = ""
    def set(self, msg):
        self.strName = msg
    def print(self):
        print(self.strName)

g = Demostring()
g.set("멤버변수에 셋팅")
g.print()
