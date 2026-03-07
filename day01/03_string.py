# 문자열 관련 메서드
# s.upper() / s.lower() => 대소문자 변환
# s.replace("a", "b") => 문자 치환
# s.split() => 공백 기준으로 나누기
# s.strip() => 앞뒤 공백 제거
# "구분자".join(list) => 리스트 → 문자열
# c.isdigit() => 숫자인지 확인
# c.isalpha() => 알파벳인지 확인

s = input("문자열 입력: ")

# 문제 1 — 모음 개수 구하기
count = 0
for x in s :
  if x in "aeiouAEIOU" :
    count += 1

print("모음 개수 : ", count)

# 문제 2 — 공백 제거 후 출력
space_x = "".join(s.split())

print("공백 제거 문자 : ", space_x)

# 문제 3 — 가장 많이 등장한 문자 찾기
count = {}

for c in s :
  if c in count :
    count[c] += 1
  else :
    count[c] = 1

max_char = max(count, key=lambda k: count[k])
print("가장 많이 등장한 문자 : ", max_char)

# 딕셔너리 - 키(Key)-값(Value)의 쌍을 저장하는 자료형
# ex) {Key1: Value1, Key2: Value2, Key3: Value3, ...}

# 딕셔너리 주요 코드
# dict[key] : key값에 맞는 value 반환
# dict.get(key, default) : key 값에 맞는 value 반환, 없으면 기본값 반환
# dict[key] = value : {key:value}를 추가
# del dict[key] : 해당하는 key:value 제거
# dict.clear() : 모든 key와 value 제거
# len(dict) : 딕셔너리 길이 반환
# dict.items() : (key, value)를 튜플로 묶어 반환
# dict.keys() : key값을 묶은 객체 반환
# dict.values() : value값을 묶은 객체 반환
# key in dict : 딕셔너리에 해당 key가 있는지 확인

# 문제 4 — 문자열에서 숫자만 추출하기
nums = []
for num in s :
  if num.isdigit():
    nums.append(num)

print("추출된 숫자 : ", "".join(nums)) 

# 문제 5 — 단어 개수 세기
word_list = s.split()
print("단어 개수 : ", len(word_list))

