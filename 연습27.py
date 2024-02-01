#연습27.py

a = "안녕하세요. 저는 김제형입니다."
print(a.count('요'))

b= "hobby"
print(b.count("h"))

c = "Python is the best choice" #위치 알려주기
print (c.find("P"))
print (c.find("t"))
print (c.find("c"))
print (c.find("o"))

d = "Life is too short" #위치 알려주기 2
print(d.index("t"))
print(d.index("s"))
print(d.index(" "))
print(d.index("i"))

f = "abcd"
print(",".join("abcd")) #문자열 삽입

print(b.upper()) #소문자를 대문자로 바꾸기

e = " LOVE "
print (e.lower()) # 대문자를 소문자로 바꾸기
print(e.lstrip()) # 오른쪽 공백 지우기
print(e.strip()) # 양쪽 공백 지우기

print(d.replace("Life", "Your leg")) #문자열 바꾸기
print(d.split()) #문자열 나누기

g = "a:b:c:d"
print(g.split(":")) #문자열 나누기