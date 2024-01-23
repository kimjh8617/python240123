#test2.py

#참조는 복사해서 전달한다.

phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print(phone)
print("park" in phone)
print("max" not in phone)

p=phone
print(id(phone), id(p))
p["moon"] = "010-1234-1234"
print(phone)
print(p)



my_list = [1,2,3,4,5]
print("List:", my_list)

my_list.append(6)
my_list.remove(2)
print("List2:", my_list)



test1 = [1,2,3,4]
test2 = [5,6,7,8]

test1 += test2

print(test1)


