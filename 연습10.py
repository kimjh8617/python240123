#연습10.py

strA = "파이썬은 강력해"
strB = "python is very powerful"

print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.count("p"))
print(strB.count("p, 7"))



strC = """결함의 원인은\n
전기차의 높은 토크를 고려하지 않은 설계와 부적절한 부품 사용. 
차축과 바퀴를 고정하는 볼트가 느슨해지면서 달리는 차에서 바퀴가 
빠지는 치명적인 오류가 발생한 것이다. 
적기생산방식(JIT)을 바탕으로 ‘품질의 대명사’로 
불려왔던 토요타는 제대로 체면을 구겼다."""
# print(strC)
print(len(strC))
print(strC.count("바퀴"))



print("---시작패턴과 끝패턴을 체크---")
print(strB.startswith("python"))
print(strB.endswith("ful"))

print("---대문자로 변환하고 소문자로 변환---")
result = strB.upper()
print(result)
print(result.lower())



print("---알파벳과 숫자로만 구성되어 있는지")
print("MBC2508".isalnum())
print("MBC:2580".isalnum())
print("2580".isalnum())

print(strC.isalnum())





print("---앞뒤에 있는 불필요한 문자열 잘라내기---")
data = "<<<피자 햄버검 치킨 >>>"
result2 = data.strip("<> ")

print(result2)





print("---문자열을 리스트로 변환하고 다시 합치기---")
lst = result2.split()
print("list : {0}".format(lst))
result3 = "".join(lst)
print("다시 하나로 조립 : {0}".format(result3))
