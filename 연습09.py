#연습09.py

#서식지정하기 

print("---서식지정하기---")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(1500000))


# #파일 생성 읽기 쓰기 작업
# f = open(file, mode)

#파일 입출력하기
print("---파일쓰기---")
f = open("c:\\work\\연습.txt", "wt")
f.write("첫 번째\n두 번째\n세 번쩨\n")
f.close()

print("---파일읽기---")
f = open("c:\\work\\연습.txt", "rt")
result = f.read()
print(result)
f.close

print("---readline() 메서드 호출---")
# 파일포인터를 다시 처음으로 이동
f.seek(0)
print(f.readline(), end = "")
print(f.readline(), end = "")

print("---readlines() 메서드 호출---")
f.seek(0)
lst = f.readlines()
print(lst)
for item in lst: 
    print(item, end = "")

#읽기 작업이 다 끝나면 마지막에 닫기
f.close