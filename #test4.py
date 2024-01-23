#test4.py

print(111)
print(1111111)


print ("---반복구문---")
value = 5
while value > 0:
    print(value)
    value -=1

print ("---for in---")
lst = ["문자열", 100, 3.14]
for item in lst:
    print(item, type(item))

lst = list( range(1,11))
print(lst)
for item in lst:
    print("Item : {0}".format(item))