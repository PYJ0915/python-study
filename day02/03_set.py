# set(집합) - 중복을 허용하지 않고(고유성), 순서가 없는(unordered) 요소를 저장하는 변경 가능한(mutable) 집합 자료형

# 핵심 특징 2가지
# 1. 중복 제거
# 2. 순서 없음 
nums = [1, 1, 2, 2, 3, 3]

s = set(nums) # 리스트 → set (중복 제거)
print(s) # {1, 2, 3}

l = list(s) # set → 리스트로 다시 변환
print(l) # [1, 2, 3]

# set(집합) 연산

a = {1, 2, 3}
b = {2, 3, 4}

print(a & b) # 교집합 → {2, 3}
print(a | b) # 합집합 → {1, 2, 3, 4}
print(a - b) # 차집합 → {1}

# 요소 추가 / 제거
s.add(4) # 추가 → {1, 2, 3, 4}
s.remove(2) # 제거 → {1, 3, 4}
2 in s # 포함 여부 확인 → true/false

# 연습문제

# 문제 3 — 중복 제거 후 정렬하여 출력
num_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]

# num_set = set(num_list)
# print(sorted(num_set))

# 한 줄 풀이
print(sorted(set(num_list)))



