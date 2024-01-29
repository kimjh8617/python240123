#연습13.py
import random

print("---랜덤하게 실수 생성")
print(random.random())
print(random.random())
print("---구간을 2.0 에서  5.0으로 지정---")
print(random.uniform(2,5))
print("----randrange() 함수를 사용한 생성---")
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print("---sample()함수를 사용한 생성---")
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))


print("---python.exe파일이 없다면---")
if exists("c:\\python310\\python.exe"):
    print("파일크기 : {0}".format(getsize("c:\\python310\\python.exe")))
else:
    print("파일이 없습니다.")

#특정 파일을 실행할 경우
    system("notepad.exe")

print("현재폴더 : {0}".format(getcwd()))
chdir("..")
shdir("c:\\work")
print("현재폴더 : {0}".format(getcwd))

lst = glob.glob("*.py")
for item in lst:
    print(item)

