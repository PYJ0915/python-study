# 문제 해결

# 리스트 문제
# 문제 1. 예상 출력 결과를 작성
nums = [1, 2, 3, 4, 5]
result = [x ** 2 for x in nums if x % 2 != 0]
print(result) # 내 답: [1, 9, 25]

# 문제 2. 중복 제거 후 내림차순 정렬해서 출력
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(set(nums), reverse=True))

# 문자열 문제
# 문제 3. 예상 출력 결과를 작성
words = ["hello", "world", "python"]
result = "".join([w[0] for w in words])
print(result) # 내 답 : hwp

# 문제 4. 각 단어의 첫 글자는 대문자로 변경하고, 나머지는 소문자로 변환 후 출력
# capitalize() => 문자열의 첫 글자는 대문자로, 나머지 모든 글자는 소문자로 변환하여 새로운 문자열을 반환하는 내장 함수
s = "hELLO wORLD pYTHON"
print(" ".join([w.capitalize() for w in s.split()]))
print(s.title()) # title 메서드를 이용한 더 짧은 방법
# title() => 문자열 내 각 단어의 첫 글자를 대문자로, 나머지 글자는 소문자로 변환하여 반환하는 함수

# 딕셔너리 문제
# 문제 5. 예상 출력 결과를 작성
d = {"a": 1, "b": 2, "c": 3}
result = {k: v * 2 for k, v in d.items()}
print(result) # 내 답: {"a":2, "b": 4, "c":6}

# 문제 6. 80점 이상인 학생만 딕셔너리 컴프리헨션으로 추출
scores = {"Tom": 90, "Jane": 85, "Mike": 92, "Anna": 88}
print({k: v for k, v in scores.items() if v >= 80})