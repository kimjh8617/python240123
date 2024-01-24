# 주민번호체크.py

import re

print("-----주민번호 체크-----")

def check_korean_resident_number(resident_number):
    # 주민번호를 검증하는 정규표현식
    pattern = r'^\d{6}-?[1-4]\d{6}$'

    # 주민번호 검증
    match = re.match(pattern, resident_number)

    if match:
        return True
    else:
        return False

# 샘플 주민번호 10개 생성
sample_resident_numbers = [
    "123456-1234567",
    "987654-9876543",
    "1234567890123",
    "111111-1111111",
    "999999-9999999",
    "890101-2345678",
    "761212-3456789",
    "820303-1234567",
    "950505-2345678",
    "880808-3456789",
]

# 각 주민번호에 대해 체크 후 결과 출력
for resident_number in sample_resident_numbers:
    result = check_korean_resident_number(resident_number)
    print(f"{resident_number}: {'Valid' if result else 'Invalid'}")
