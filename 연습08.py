#연습08.py

#Chap 05 정렬 방식 지정하기.py
for x in range(1,10):
    print(x, "*", x, "=", x*x)

print("__오른쪽 정렬__")
for x in range(1,10):
    print(x, "*", x, "=", str(x*x).rjust(3))

print("__앞쪽에 0으로 채우기__")
for x in range(1,10):
    print(x, "*", x, "=", str(x*x).zfill(3))


# 아래와 같이 str() 함수 또는 str()클래스의 생성자(초기화 메서드)를 사용해서
# 문자열(str)로 변환하면, 문제없이 문자열로 연결됩니다.
url = "https://www.python.org/?page=" + str(1)
print(url)
