# 실습문제
import re
from contextlib import contextmanager

# 문제 1 - 아래 텍스트에서 날짜를 전부 추출해봐요.
text = "회의: 2026-03-17, 마감: 2026-04-01, 출시: 2026-12-25"
result = re.findall(r"\d{4}-\d{2}-\d{2}", text)
print(result)

# 문제 2 - 아래 텍스트에서 이메일 아이디 부분만(@ 앞부분) 추출
text = "hello@gmail.com world@naver.com python@daum.net"
result = re.findall(r"[\w]+@", text)
print(result)

# 문제 3 - @contextmanager 를 활용해서 코드 실행 전후에 아래처럼 출력하는 컨텍스트 매니저 log_context 만들기
@contextmanager
def log_context(s):
  print("[시작]", s)
  try:
    yield
  finally:
     print("[완료]", s)

with log_context("데이터 처리"):
    print("처리 중...")

# [시작] 데이터 처리
# 처리 중...
# [완료] 데이터 처리

# 문제 2번 개선 - findall의 경우 그룹이 있으면 그룹만 반환!
# () 로 원하는 부분만 감싸기
text = "hello@gmail.com world@naver.com python@daum.net"
result = re.findall(r"([\w]+)@", text)
print(result) # ['hello', 'world', 'python']