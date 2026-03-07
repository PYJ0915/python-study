from collections import Counter

sentence = input("문장을 입력하세요 : ")

words = sentence.split()
word_set = set(words)

# count = dict(Counter(words)) <- dict 변환하지 않아도 됨!
# Counter는 dict를 상속 받아 items(), keys(), values(), max() 전부 사용 가능!

count = Counter(words)

print("단어 개수 : ", len(words))
print("중복 제거 단어 : ", list(word_set))
print("가장 많이 등장한 단어 : ", max(count, key=lambda w: count[w]))
print("단어 길이 정렬 : ", sorted(word_set, key=len))
print("단어 빈도 수 출력")
for k, v in count.items() :
  print(k, ":", v)

# 좀 더 간결한 풀이 (파이써닉)
print("가장 긴 단어 : ", max(word_set, key=len))
print("가장 짧은 단어 : ", min(word_set, key=len))

# 내 풀이 
# print("가장 긴 단어 : ", sorted(word_set, reverse=True, key=len)[0])
# print("가장 짧은 단어 : ", sorted(word_set, key=len)[0])

# 내 풀이
# print("단어 빈도수 내림차순 출력")
# sort_count = sorted(count.items(), key=lambda x : x[1], reverse=True)
# for c in sort_count :
#   print(c[0], ":", c[1])

# 튜플 언패킹을 활용한 더 간결한 풀이 (파이써닉)
print("단어 빈도수 내림차순 출력")
for k, v in sorted(count.items(), key=lambda x: x[1], reverse=(True)) :
  print(k, ":", v)

# 가장 많이 등장한 문자 (공백 제거 포함! -> 공백이 나올 가능성 O)
print("가장 많이 등장한 문자 : ", Counter(sentence.replace(" ", "")).most_common(1)[0][0])

# 문자 빈도수 상위 3개 출력 (공백 제거 포함! -> 공백이 나올 가능성 O)
print("문자 빈도수 상위 3개 : ", Counter(sentence.replace(" ", "")).most_common(3))