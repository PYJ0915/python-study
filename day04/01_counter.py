# counter - 반복 가능한(iterable) 객체의 요소 빈도수를 딕셔너리 형태로 아주 쉽게 계산해주는 강력한 클래스

# counter 임포트
from collections import Counter

# 문자열 빈도수
word = "banana"
freq = Counter(word)

print(freq) # Counter({'a': 3, 'n': 2, 'b': 1})
print(dict(freq)) # {'b': 1, 'a': 3, 'n': 2}

# 리스트 빈도수
nums = [1, 2, 2, 3, 3, 3, 4]
freq = Counter(nums)

print(freq) # Counter({3: 3, 2: 2, 1: 1, 4: 1})
print(dict(freq)) # {1: 1, 2: 2, 3: 3, 4: 1}

# most_common() — 자주 등장한 순서대로
freq = Counter("banana")

print(freq.most_common(1)) # [('a', 3)] ← 1위만
print(freq.most_common(2)) # [('a', 3), ('n', 2)] ← 1~2위
print(freq.most_common()) # 전체 내림차순

# 기존 방식과 비교

# 기존 방식
freq = {}
for c in word:
    freq[c] = freq.get(c, 0) + 1

# Counter 한 줄로
freq = Counter(word)

# 연습문제

# 문제 1 — 문자 빈도수 구하기
word = "apple"
freq = Counter(word)
print(dict(freq))

# 문제 2 — 가장 많이 등장한 숫자
nums = [1, 2, 2, 3, 3, 3, 4]
print(Counter(nums).most_common(1))