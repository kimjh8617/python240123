#연습32.py

#집합 자료형은 어떻게 만들까?
s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2)

# set 중복을 허용하지 않으며, 순서가 없다. 
l1 = list(s1)
l2 = list(s2)
print(l1)
print(l2)
print(l1[0])


#교집합, 합집합, 차집합 구하기
d1= set ([1,2,3,4,5,6])
d2= set ([4,5,6,7,8,9])
print(d1 & d2)
print(d1.intersection(d2)) #교집합 구하기

print(d1 | d2)
print(d1.union(d2)) #합집합 구하기

print(d1 - d2)
print(d1 - d2) # 차집합 구하기
print(d1.difference(d2))


s1.update([4,5,6,7,8])
print(s1)

#특정 값 제거하기 - remove
s1.remove(4)
print(s1)

