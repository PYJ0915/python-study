# 딕셔너리 심화
# 1. 복습
d = {}
d["key"] = "value"
d.get("key", "기본값")  # 키값 없으면 기본값 반환
"key" in d  # 키 존재 확인

# 2. 심화
# 1) defaultdict - 키 없어도 기본값 자동 생성
from collections import defaultdict

d = {}
d = defaultdict(int)  # 기본값 0
d["apple"] += 1
d["apple"] += 1
d["banana"] += 1
print(dict(d)) # {'apple': 2, 'banana': 1}

d = {}
d = defaultdict(list) # 기본값 []
d["a"].append(1)
d["a"].append(2)
d["b"].append(3)
print(dict(d))  # {'a': [1, 2], 'b': [3]}

# 2) OrderedDict - 삽입 순서 보장
from collections import OrderedDict
od = OrderedDict()
od["b"] = 2
od["a"] = 1
od["c"] = 3
print(list(od.keys()))  # ['b', 'a', 'c']

# 3) 빈도수 세기
from collections import Counter

words = ["apple", "banana", "apple", "kiwi", "banana", "apple"]
freq = Counter(words)
print(freq) # Counter({'apple': 3, 'banana': 2, 'kiwi': 1})
print(freq.most_common(2))  # [('apple', 3), ('banana', 2)]

# 4) 그룹핑
from collections import defaultdict

students = [
    ("Tom", "A"),
    ("Jane", "B"),
    ("Mike", "A"),
    ("Anna", "B"),
    ("John", "C"),
]

groups = defaultdict(list)
for name, dept in students:
  groups[dept].append(name)

print(dict(groups))   # {'A': ['Tom', 'Mike'], 'B': ['Jane', 'Anna'], 'C': ['John']}

# 5) 딕셔너리 병합
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
merged = a | b  # b가 우선!
print(merged)   # {'x': 1, 'y': 3, 'z': 4}

# 3. 해시 활용 알고리즘 패턴
# 1) 두 수의 합 - O(n)
def two_sum(nums: list, target: int) -> list:
  seen = {}
  for i, n in enumerate(nums):
    complement = target - n
    if complement in seen:
      return [seen[complement], i]
    seen[n] = i
  return []

print(two_sum([2, 7, 11, 15], 9))   # [0, 1]

# 2) 중복 찾기 - O(n)
def find_duplicates(nums: list) -> list:
  seen = set()
  result = []
  for n in nums:
    if n in seen:
      result.append(n)
    seen.add(n)
  return result

print(find_duplicates([1, 2, 3, 2, 4, 3]))  # [2, 3]