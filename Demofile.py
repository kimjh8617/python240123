# Demofile.py

#파일 쓰기
f = open("demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일 읽기
f = open("demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)

#다시 처음으로 파일 포인터 이동
f.seek(0)
#한 번에 한 출을 읽어서 처리
print(f.readline(), end="")
print(f.readline(), end="")

#전체를 리스트로 리턴
f.seek(0)
lst =f.readlines()
print(lst)


f.close()

# read() : 파일 전체를 읽어서 문자열로 반환한다.
# readline() : 한 줄씩 읽은 문자열을 반환한다.
# readlines() : 파일의 모든 내용을 줄 단위로 잘라서 반환한다. 리턴형식이 리스트 형식이다. 

# f.close()
# f = open("")
# f.read 

encode encode encode encode 







