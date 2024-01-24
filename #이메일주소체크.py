#이메일주소체크.py
import re

def check_email_address(email):
    # 이메일 주소를 검증하는 정규표현식
    # raw string notation : 날것 그대로 표기
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # 이메일 주소 검증
    match = re.search(pattern, email)

    if match:
        return True
    else:
        return False

# 샘플 이메일 주소 10개 생성
sample_emails = [
    "user@example.com",
    "john.doe123@gmail.com",
    "test.email@domain.co.uk",
    "invalid_email@.com",
    "missing_at_symbol.com",
    "user@company",
    "name@server123",
    "email_with space@example.com",
    "user@localhost",
    "user@.co",
]

# 각 이메일 주소에 대해 체크 후 결과 출력
for email in sample_emails:
    result = check_email_address(email)
    print(f"{email}: {'Valid' if result else 'Invalid'}")
