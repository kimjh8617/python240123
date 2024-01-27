#연습06.py

def __testFunction():
    print("모듈 내부에서만 사용")

def intersection(listX, listY):
    result = []
    for x in listX:
        result.append(x)

    return result

def union(*tp):
    result = []
    for item in tp:
        for x in item:
            if not x in result:
                result.append(x)
    return result


print("모듈이 로딩됩니다.")
x = 2 
def print():
    print("x={0}".format(x))

