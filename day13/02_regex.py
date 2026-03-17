# 정규표현식(re 모듈) - 문자열에서 패턴을 찾는 방법
# 1. 정규 표현식
import re

text = "전화번호: 010-1234-5678"
print(re.search(r"\d{3}-\d{4}-\d{4}", text)) # <re.Match object; span=(6, 19), match='010-1234-5678'>
# 010-1234-5678 찾기
# r"..." — raw string \n 을 줄바꿈이 아닌 문자 그대로 인식

# 2. 자주 쓰는 패턴
# 문자 종류
# \d        # 숫자 [0-9]
# \D        # 숫자 아닌 것
# \w        # 문자 + 숫자 + _ [a-zA-Z0-9_]
# \W        # 문자 + 숫자 + _ 아닌 것
# \s        # 공백 (스페이스, 탭, 줄바꿈)
# \S        # 공백 아닌 것
# .         # 아무 문자 1개 (줄바꿈 제외)

# 반복
# *         # 0번 이상
# +         # 1번 이상
# ?         # 0번 또는 1번
# {n}       # 정확히 n번
# {n,m}     # n번 이상 m번 이하

# 위치
# ^         # 문자열 시작
# $         # 문자열 끝

# 묶음
# [abc]     # a 또는 b 또는 c
# [a-z]     # a 부터 z 까지
# [A-Z]     # A 부터 Z 까지
# [0-9]     # 0 부터 9 까지
# [^abc]    # a, b, c 제외한 모든 문자

# 3. re 모듈 주요 함수
text = "apple 123 banana 456"
# 1) search - 첫 번째 매칭 찾기(위치 상관 X)
m = re.search(r"\d+", text)
print(m.group()) # 123
print(m.start()) # 6 ← 시작 인덱스
print(m.end())   # 9 ← 끝 인덱스

# 2) findall - 모든 매칭 리스트로 반환
print(re.findall(r"\w+", text))   # ['apple', '123', 'banana', '456']

# 3) match - 문자열 시작부터만 매칭
m = re.match(r"\d+", text)
print(m) # None ← 시작이 숫자가 아님
m = re.match(r"\w+", text)
print(m.group()) # apple

# 4) sub - 매칭된 부분 치환
print(re.sub(r"\d+", "###", text)) # apple ### banana ###

# 5) split - 패턴 기준으로 분리
print(re.split(r"\s+", text)) # ['apple', '123', 'banana', '456']


# 4. search vs match 차이
text = "hello 123"
print(re.search(r"\d+", text).group()) # 중간에서도 찾음 → 123
print(re.match(r"\d+", text)) # 시작부터 매칭 안 됨 → None
print(re.match(r"\w+", text).group()) # 시작부터 매칭 → hello

# 5. 그룹 - 패턴 일부만 추출
text = "2026-03-17"

# 그룹 없이
m = re.search(r"\d{4}-\d{2}-\d{2}", text)
print(m.group())  # 2026-03-17
# print(m.group(1))  # IndexError: no such group

# 그룹으로 나누어 추출
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
print(m.group(0))  # 2026-03-17
print(m.group(1))  # 2026
print(m.group(2))  # 03
print(m.group(3))  # 17

# 6. 실전 활용 예제
# 이메일 추출
text = "문의 : hello@gmail.com 또는 world@naver.com"
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
print(emails)

# 전화번호 추출
text = "010-1234-5678 또는 02-123-4567"
phones = re.findall(r"\d{2,3}-\d{3,4}-\d{4}", text)
print(phones)

# 숫자만 제거
text = "abc123def456"
print(re.sub(r"\d", "", text)) # "abcdef"

# 공백 여러 개 → 하나로
text = "hello      world      python"
print(re.sub(r"\s+", " ", text))