# 정렬 응용

# 딕셔너리 value 기준으로 정렬
freq = {'a': 3, 'b': 1, 'c': 2}

# 오름차순
print(freq.items()) # dict_items([('a', 3), ('b', 1), ('c', 2)]) -> key와 value를 튜플로 묶어 뷰라는 객체로 반환
print(sorted(freq.items(), key=lambda x: x[1]))

# 내림차순
print(sorted(freq.items(), key=lambda x: x[1], reverse=True))

# 애너그램(문자 구성이 같은 문자열) 검사
s1 = "listen"
s2 = "silent"

# 방법 1 - 두 문자열을 정렬 후 비교
print(sorted(s1) == sorted(s2))

# 방법 2 - Counter를 통해 빈도수로 비교
from collections import Counter
print(Counter(s1) == Counter(s2))


# 연습 문제

# 문제 3 — 애너그램 검사
s1 = "listen"
s2 = "silent"

# 방법 1 - 정렬
print(sorted(s1) == sorted(s2))

# 방법 2 - counter
print(Counter(s1) == Counter(s2))

# 문제 4 — 딕셔너리 value 기준 내림차순 정렬
freq = {'a': 3, 'b': 1, 'c': 2}
print(sorted(freq.items(), key=lambda x : x[1], reverse=True))

# 문제 5 - 애너그램 공백/대소문자 처리
s1 = " L i s t e n "
s2 = " S i l e n t "

print(sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower()))