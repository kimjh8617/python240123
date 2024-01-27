#연습12.py

import time

print(time.time())
time.sleep(5)
print(time.time())

print("---표준시간---")
print(time.gmtime())
print("---한국시간---")
print(time.localtime())


#datetime 모듈
from datetime import *

d1 = date(2023, 6 ,1)
print(d1)
print("---오늘날짜를 리턴---")
d2 = date.today()
print(d2)
print("100일을 더하면 : {0}".format(d2))
d3 = timedelta(days=100)
print(d2 + d3)
d4 = datetime.now()
print("현재 날짜와 시간을 출력 :{0}".format(d4))
