# test3.py

#함수정의
def setValue(newValue):
    #지역변수
    x = newValue
    print("지역변수 x:", x)

#호출
retValue = setValue(5)
print(retValue)

#함수정의

def swap(x,y):
    return y,x


print(swap(5,6))


x = 10 
y = 20

def func():
    return x+y

print(func())

def func2():
    x = 1
    return x+y

print(func2())




#함수정의
def times(a=10, b=20):
    return a*b
print(times())
print(times(5))
print(times(5,6))




#가변인자
def union(*tp):
    result = []
    for item in tp:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM", "SPAM"))
print(union("HAM", "SPAM", "EGG"))



#람다함수


