# 1부 - 코드 보고 출력 결과 예측하기
# 문제 1 - O
nums = [1, 2, 3, 4, 5]
nums.insert(2, 10)
nums.pop(0)
print(nums) # 내 답 : [2, 10, 3, 4, 5]

# 문제 2 - X
a = [1, 2, 3]
b = a
b.append(4)
print(a) # 내 답 : [1, 2, 3]

# 문제 3 - O
words = ["apple", "banana", "kiwi"]
# 1단계 — 길이 4 초과 필터링
result = [w for w in words if len(w) > 4]
# 2단계 — 역순 정렬 (알파벳 기준)
result.sort(reverse=True)
print(result) # 내 답 : ["banana", "apple"]

# 문제 4 - O
nums = [1, 2, 3, 4, 5]
print(nums[::2]) # 내 답 : [1, 3, 5]
print(nums[::-1]) # 내 답 : [5, 4, 3, 2, 1]

# 오답 정리
a = [1, 2, 3]
b = a # ← a랑 b가 같은 리스트를 가리킴
b.append(4) # b를 수정하면 a도 같이 바뀜
print(a) # [1, 2, 3, 4]

# 자바에서도 같은 개념
# int[] a = {1, 2, 3};
# int[] b = a; 참조 복사
# b[0] = 99;
# System.out.println(a[0]); 99

# 복사가 필요하다면
b = a.copy()    # 독립적인 복사본
b = a[:]        # 슬라이싱으로 복사

# 2부 - 문제 해결
# 문제 5 — 리스트에서 가장 작은 값 찾기 - O
nums = [5, 3, 9, 1, 4]
print(min(nums))

# 문제 6 — 문자열이 회문인지 검사 - O 
s = "level"
print(s == s[::-1])

# 문제 7 — 리스트에서 중복된 값만 추출 - X
from collections import Counter
nums = [1, 2, 2, 3, 3, 3, 4]
count = Counter(nums)
print([k for k, v in count.items() if v != 1])

# 오답 정리
# 틀린 코드
print(k for k, v in count.items() if v != 1)
# generator object <genexpr> at 0x... 출력

# 리스트 컴프리헨션
print([k for k, v in count.items() if v != 1])
# [2, 3]

[x for x in nums]   # [] → 리스트 컴프리헨션
(x for x in nums)   # () → 제너레이터 (지금 단계에선 안 씀)
{x for x in nums}   # {} → 셋 컴프리헨션

# 핵심 - 컴프리헨션 쓸 때 리스트로 만들려면 항상 []