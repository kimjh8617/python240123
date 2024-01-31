#연습26.py

print("{0:<10}".format("hi")) #왼쪽 정렬

print("{0:>10}".format("hi")) #오른쪽 정렬

print("{0:^10}".format("hi")) #가운데 정렬

print("{0:=^10}".format("hi")) #공백 채우기1

print("{0:!<10}".format("hi")) #공백 채우기2

a = "안녕하세요. 저는 김제형입니다."
print(a.count('요'))

b= "hobby"
print(b.count("y"))

c = "Python is the best  choice"
print (a.find("P"))
print (a.find("t"))
print (a.find("c"))
print (a.find("o"))