#연습28.py

#리스트는 어떻게 만들고 사용할까?

리스트명 = [1,2,3,4,5,6,7,8,9]
print(리스트명)

#여러가지 리스트의 생김새.

# a = []
# b = [1,2,3]
# c = ['Life', 'is', 'too', 'short']
# d = [1,2,"dins", "gins"]
# e = [1,2,['Love is Always makes happy to us']]

# print(a,b,c,d,e)

# print("---리스트의 인덱싱과 슬라이싱---")
# print(b[0])
# print(b[1])
# print(b[2])

# print(b[1] + b[2])

f = [1,2,3, ["a", "b" ,"c"]]
print(f[1])
print(f[0])
print(f[-1])
print(f[3])
print(f[-1][0])
print(f[-1][1])
print(f[-1][2])

print("---리스트의 슬라이싱---") #슬라이싱은 '잘라 낸다'라는 뜻
g = [1,2,3,4,5,6,7,8,9]
print(g[0:4]) #4 전까지만 슬라이싱 해줌
print(g[0:7])
print(g[3:8])
print(g[1:6])

h  = "12345"
print(h[0:2])

print(g[:6])
print(g[3:])

# print("---리스트 연산---")
# a = [1,2,3]
# b = [4,5,6]

# print(a+b)
# print(a*2)
# print(len(a+b))

# #리스트의 수정과 삭제
# a[2] = 7
# print(a) #리스트의 값 수정하기
# del a[1] #삭제 del 객체 
# print(a)

print("---리스트에 요소 추가하기---")
my_list = [1,2,3]
my_list.append(5)
my_list.append([7,8])
print(my_list)


print("---리스트 정렬---")
a = [1,4,7,2,9,8,3,5,0,6]
a.sort()
print(a)

b = ["a","c","b","g","e","f","d"]
b.sort()
print(b)

print("---리스트 뒤집기---") #reverse
c = ["a","b","c","d","e","f","g","h"]
c.reverse()
print(c)

print("---인덱스 반환---") #/????????????
d = [1,2,3]
d.index(2)
print(d)