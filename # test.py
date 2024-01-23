# test.py



x = 1000
y = 3.14

print(type(x))
print(type(y))

strA = "python is very powerful"
strB = "파이썬은 강력해"

print(type(strA))
print(type(strB))


strC = """다중 라인으로 저장할 경우
이렇게 묶으면
다중 라인으로 인식합니다."""

print(strC)





strD = "LOVER IS MECGICAL"
strE = "사랑은 언제나 돌아오는 거야!"

print(strD[0])
print(strE[4])



strF = "양자심리학"
print(strF[-1])


strG = "말할 수 없는 것에 대해 우리는 침묵해야 한다."
print(strG[-7:])

#List, Tuple, Set, Dict 형식 사용하기

lst = [1,2,3,4,5]
print(type(lst))
print(len(lst))
print(lst)

#리스트 입력, 수정, 삭제하기
lst.append(6)
lst.insert(3,20)
lst[0] = 100
lst.remove(5)
print(lst)

print(18*4)



tp = (100,200,300)
print(len(tp))
print(tp.index(100))
print(tp.count(300))
print("id: %s, name: %s" % ("kim", "김제형"))


#print("id=$s, name: %s" % ("kim"), "김제형"))

#함수정의

def times(a,b):
    return a+b, a-b, a*b, a//b

#호출
result=times(178,42)
print(result)


def test(a,b,c):
    return (a*c)-b

result=test(243,32,190)
print(result)


device={"아이폰":5, "아이패드":10, "윈도우노트북":20}
print(device)
print(type(device))
print(len(device))

print(device["아이폰"])
device["맥북"]=70
device["아이폰"]=50
del device["아이패드"]
print(device)



