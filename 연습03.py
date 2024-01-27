#연습03.py

class DemoClass:
    def __init__(self, value):
        self.value = value
        print("인스턴스가 생성되었습니다. value : ", value)
    def __del__(self):
        print("인스턴스가 소멸되었습니다.")

d = DemoClass(5)
del d

print("전체 코드 실행 종료")
