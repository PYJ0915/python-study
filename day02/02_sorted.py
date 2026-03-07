# 파이썬 정렬
arr = [5, 1, 9, 3]

print(sorted(arr)) # 오름차순 정렬 (기본값)
print(sorted(arr, reverse=True)) # 내림차순

# sorted()와 sort()
sorted(arr) # 새 리스트 반환
arr.sort() # 원본을 직접 수정

# cf) 자바 => Collections.sort(list);

# sort 활용 예시
words = ["hi", "python", "cat"]

# 문자열 길이 기준 정렬
print(sorted(words, key=len)) # ['hi', 'cat', 'python']

# lamda로 직접 기준 지정 정렬 (문자열 길이)
print(sorted(words, key=lambda x: len(x)))

# 연습 문제
word_list = ["apple", "banana", "kiwi", "grape", "melon"]

# 문제 1 — 문자열 길이 기준으로 정렬
print(sorted(word_list, key=len))

# 문제 2 — 길이가 5 이상인 단어만 출력
for word in word_list :
  if len(word) >= 5 :
    print(word)