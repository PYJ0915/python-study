# 문제 1 - 리스트를 내림차순 정렬
nums = [8, 3, 5, 1, 9]
print(sorted(nums, reverse=True))

# 문제 2 - 문자열 길이 기준 정렬
words = ["apple", "kiwi", "banana", "grape"]
# print(sorted(words, key=lambda x: len(x)))
print(sorted(words, key=len))

# 문제 3 - 중복 제거 후 정렬
num_list = [1,1,2,3,3,4,4,5]
print(sorted(set(num_list)))

# 문제 4 - zip으로 딕셔너리 만들기
names = ["Tom", "Jane", "Mike"]
scores = [80, 95, 70]
print(dict(zip(names, scores)))

# 문제 5 - enumerate 사용해서 출력
fruits = ["apple", "banana", "orange"]
for i, v in enumerate(fruits) :
  print(i, v)

# 문제 6 - 문자열 길이 내림차순으로 정렬
word_list = ["cat", "apple", "banana", "hi"]
# print(sorted(word_list, key=lambda x: -len(x)))
print(sorted(word_list, key=len, reverse=True))
