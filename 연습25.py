#연습25.py

# a = "Life is too short, You need Python"
# print(a[3])
# print(a[1])
# print(a[7])
# print(a[3])
# print(a[8])
# print(a[3])
# print(a[9])


# b = "Life is too short"
# print(len(b))
# print(b[0:5])
# print(b[0:1])
# print(b[0:3])
# print(b[0:4])
# print(b[0:2])
# print(b[9:])
# print(b[:7])
# print(b[:])

# c = "20240130Rainy"
# date = a[:9]
# weather = a[8:]
# print(c)
# print(weather)

a = "20240130Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

b="Pithon"
print(b[1])

# %s 문자열
# %c 문자 1개
# %d 정수
# %f 부동소수
# %o 8진수
# %x 16진수

d="I eat %d apples."
print(d % 3)
d1="I eat %s apples."
print(d1 % "five")
d2="I eat %d apples."
num= 4
print(d2 % num)


d3 = "I ate %d apples. so I was sick for %s days"
num1 = 10
day = "three"
print(d3 % (num, day))

#format 함수를 사용한 포매팅

d4 = "I like {0} apples."
print(d4.format(4))

d4 = "I like {0} apples."
print(d4.format(50))

d4 = "I like {0} apples."
print(d4.format(100000))

d4 = "I like {0} apples."
print(d4.format(3284356))

d4 = "I like {0} apples."
print(d4.format(43425))

print("----문자열 바로 대입하기----")
print(d4.format("four"))
print(d4.format("six"))
print(d4.format("숫자 안 알려줌"))
print(d4.format("오백개"))
print(d4.format("ten"))


print("---숫자 값을 가진 변수로 대입하기---")
num2 = 752
print(d4.format(num2))




print("---2개 이상의 값 넣기---")
num3 = 10
day1 = "three"
d5 = "I ate {0} apples. So I was sick for {1} days"
print(d5.format(num3, day1))

num4 = 8935
day1 = "ten"
d5 = "I ate {0} apples. So I was sick for {1} days"
print(d5.format(num3, day1))



num5 = 15
d6 = "나는 {0}개의 요구르트를 먹었고, {day2} 일 간 화장실에서 살다시피 했다."
print(d6.format(num5 , day2=3))




