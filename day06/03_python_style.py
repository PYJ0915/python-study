# 핵심 3가지 복습 및 심화

# 1️⃣ zip + 리스트 컴프리헨션
a = [1, 2, 3]
b = [4, 5, 6]

# 요소 합
print([x + y for x, y in zip(a, b)]) # [5, 7, 9]
# 요소 곱
print([x * y for x, y in zip(a, b)]) # [4, 10, 18]

# 2️⃣ enumerate + 조건
words = ["apple", "hi", "banana", "cat"]

# 인덱스가 짝수인 단어만
print([v for i, v in enumerate(words) if i % 2 == 0]) # ["apple", "banana"]

# 3️⃣ sorted + lambda 심화
data = [("Tom", 90), ("Jane", 85), ("Mike", 92)]

# 점수 기준 내림차순
print(sorted(data, key=lambda x: x[1], reverse=True))
# [("Mike", 92), ("Tom", 90), ("Jane", 85)]

# 이름 길이 기준
print(sorted(data, key=lambda x : len(x[0])))
# [("Tom", 90), ("Jane", 85), ("Mike", 92)]


# 연습 문제
# 문제 1 - 2 예상 출력 결과 작성
a = [1, 2, 3]
b = [10, 20, 30]
result = [x * y for x, y in zip(a, b)]
print(result) # 내 답 : [10, 40, 90]

words = ["apple", "hi", "banana", "cat", "kiwi"]
result = [v for i, v in enumerate(words) if i % 2 != 0]
print(result) # 내 답 : ["hi", "cat"]

# 문제 3 - 4 직접 구현
# 문제 3. 점수 기준 오름차순 정렬
data = [("Tom", 90), ("Jane", 85), ("Mike", 92)]
print(sorted(data, key=lambda x : x[1]))

# 문제 4. 평균 이상인 점수만 리스트 컴프리헨션으로 추출
scores = [85, 92, 78, 95, 88]
print([x for x in scores if x >= sum(scores) / len(scores)])

# 문제 4 개선점
# sum(scores) / len(scores) 가 반복문 돌 때마다 계산
avg = sum(scores) / len(scores)
print([x for x in scores if x >= avg])