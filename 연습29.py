# #연습29.py

# print("---인덱스 반환---") #/????????????
# d = [1,2,3]
# print(d.index(2))

# # print("---리스트에 요소 삽입---")
# # a= [1, 2, 3]
# # a.insert(3, 5)
# # print(a)

# # print("---리스트 요소 제거---")
# # b = [1,2,3,4,5,6]
# # b.remove(4)
# # print(b)

# # print("---리스트 요소 끄집어 내기---")
# # c = [1,2,3]

# # # c.pop(1)
# # print(c.pop(1))

# d = [1,2,5,4,234,1,3,34,645,2,1,124,32,64,65,8,2,1,1,456,4,23]
# print(d.count(5))

#리스트 확장
print("---리스트 확장---")
a = [1, 2, 3]
a.extend([4,5])
print(a)

# print(a.extend([6,7]))

b = [6, 7]
a.extend(b)
print(a)