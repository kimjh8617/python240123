#연습31.py

#딕셔너리는 단어 그대로 '사전'이라는 뜻이다. 
#즉 "people"이라는 단어에 "사람"
#"baseball"이라는 단어에 "야구"라는 뜻이 부합되듯이
#딕셔너리는 key와 value를 한 쌍으로 가지는 자료형이다.

# dic = {"name" : "pey", "phone" : "010-9999-1234", "birth" : "1118"}
# print(dic)

a = {1: "hi"}
a2 = { "a" : [1,2,3]}
print(a)
print(a2)


#딕셔너리 쌍 추가
a3 = {1:"a"}
a3[2] = "b"
# print(a3)

a3["name"] = "pey"
a3[3] = [1,2,3]
print(a3)

# 딕셔너리 요소
del a3[1]
print(a3)

#딕셔너리를 사용하는 방법
 
# 딕셔너리에서 key 를 사용해 value 얻기
grade = {"pey" : 10, "julliet" : 99}
print(grade["pey"])
print(grade["julliet"])

dic = {"name" : "pey", "phone" : "010-9999-1234", "birth" : "1118"}
print(dic["name"])
print(dic["phone"])
print(dic["birth"])

#key 리스트 만들기
print(dic.keys())

for k in dic.keys():
    print(k)

#value 리스트 만들기
print(list(dic.keys()))

#key, value 쌍 얻기
print(dic.values())

#쌍 모두 지우기
print(dic.items())

#key value 얻기 - get
print(dic.get("name"))
print(dic.get("phone"))

print(dic.get("nokey"))

print(dic.get("nokey", "foo"))

#해당 key가 딕셔너리 안에 있는지 조사하기 - in
print("name" in dic)
print("email" in dic)