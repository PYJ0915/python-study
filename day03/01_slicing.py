# 슬라이싱 - 연속적인 객체(문자열, 리스트, 튜플 등)에서 특정 범위를 선택해 새로운 객체를 만드는 것

s = "hello"
#    01234  ← 인덱스
  
print(s[0]) # h
print(s[4]) # o
print(s[-1]) # o
print(s[2]) # l
print(s[2]) # l

# 슬라이싱 - [시작 : 끝]
print(s[0:3]) # hel ← 0, 1, 2 (끝 인덱스 미포함)
print(s[1:4]) # ell
print(s[0:]) # hello ← 처음부터 끝까지
print(s[:3]) # hel
print(s[:]) # hello ← 전체

# 슬라이싱 - [시작 : 끝 : 간격]
print(s[::1]) # hello ← 1칸씩
print(s[::2]) # hlo ← 2칸씩(0, 2, 4)
print(s[::-1]) # olleh ← -1칸씩(-1, -2, -3, -4, -5)

# 리스트 슬라이싱
nums = [1, 2, 3, 4, 5]

print(nums[1:3]) # [2, 3]
print(nums[::-1]) # [5, 4, 3, 2, 1]
print(nums[::2]) # [1, 3, 5]

# 슬라이싱 주요 예시
s[::-1] # 문자열 뒤집기
s == s[::-1] # 회문 검사 


