#test7.py

#함수정의
def setValue(newValue):
    #지역변수
    x = newValue
    print("지역변수 :", x)

#호출
retValue = setValue(5)
print(retValue)

#함수정의
def swap(x,y):
    return y,x

#호출
print(swap(4,5))


#전역변수
x = 10
y = 20

#함수정의
def func():
    return x+y

#호출
print(func())

#함수정의
def func2():
    x=1
    return x+y

print(func2())

#기본값명시 - 키워드인자전달
#함수정의
def times(a=10 , b=20):
    return a*b

#호출
print ( times())
print ( times(5))
print ( times(5,6))

#키워드인자전달(파라메터명을 명시)    
def connectURI(server, port):
    strURI = "http://" + "www." + server + ":" + port 
    return strURI

#호출 
print ( connectURI("naver.com", "80"))
print ( connectURI(port="8080",server = "naver.com" ))




#가변인자처리함수
def union(*tp):
    result = []
    for item in tp:
        for  x in item:
            if x not in result:
                result.append(x)
    return result

print (union("HAM", "SPAM"))
print (union("HAM", "SPAM", "EGG"))



#람다함수
g = lambda x,y:x*y
print (g(2,3))
print (g(3,5))
print ((lambda x:x*x)(3))
print (globals())


lst = [1,2,3,4,5]
def add10(i):
    return i + 10

for item in map(add10, lst):
    print(item)

