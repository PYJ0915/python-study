# 실습 문제 - 아래 조건으로 함수를 구현하시오
from collections import Counter
from collections import defaultdict
# 문제 1
# 문자열 리스트에서 애너그램끼리 그룹핑
# 애너그램 = 같은 문자로 이루어진 단어
def group_anagrams(words: list) -> list:
    groups = defaultdict(list)
    for w in words:
      key = str(sorted(w))
      groups[key].append(w)
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


# 문제 2
# 문자열에서 처음으로 반복되지 않는 문자 반환
# 없으면 None 반환
def first_unique(s: str) -> str:
  freq = Counter(s)
  for c in s:
     if freq[c] == 1:
        return c
  return None

print(first_unique("leetcode"))   # "l"
print(first_unique("aabb"))       # None


# 문제 3
# 두 문자열이 애너그램인지 확인
# 대소문자 무시
def is_anagram(s1: str, s2: str) -> bool:
    if Counter(s1.lower()) == Counter(s2.lower()):
       return True
    return False

print(is_anagram("Listen", "Silent"))   # True
print(is_anagram("hello", "world"))     # False


# 개선된 풀이
# 문제 1
def group_anagrams(words: list) -> list:
    groups = defaultdict(list)
    for w in words:
      key = "".join(sorted(w))   # "aet" ← str() 보다 간결
      groups[key].append(w)
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))

# 문제 3
def is_anagram(s1: str, s2: str) -> bool:
    return Counter(s1.lower()) == Counter(s2.lower()) 
    # 비교식을 바로 return 으로 줄일 수 있음!

print(is_anagram("Listen", "Silent"))   # True
print(is_anagram("hello", "world"))     # False