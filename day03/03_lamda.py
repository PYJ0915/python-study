# lambda - 한 줄짜리 익명함수 (일회성 함수의 경우 코드를 간결하게 하기위해 사용)

# 일반 함수
def add(x, y) :
  return x + y

print(add(3, 7)) # 10

# lambda
# lambda 매개변수 : 반환값
print((lambda x, y : x + y)(3, 7)) # 10

# 주요 사용 예시 - 정렬 기준

# 문자열 길이
words = ["apple", "cat", "banana"]
print(sorted(words, key=lambda w : len(w)))

# 딕셔너리 value
freq = {"a" : 1, "b" : 3 , "c" : 2}
print(max(freq, key=lambda k: freq[k])) # b

# 내림차순
nums = [5, 3, 2, 6, 86, 1]
print(sorted(nums, key=lambda n : -n))

# 연습문제

# 문제 1 - lambda를 활용하여 내림차순 정렬
nums = [5, 1, 9, 3]
print(sorted(nums, key=lambda n: -n))

# 문제 2 - lambda로 문자열 길이 기준 정렬
words = ["hi", "python", "cat"]
print(sorted(words, key=lambda w: len(w)))

# 문제 3 - lambda로 1의 자리 기준 정렬
nums = [10, 3, 25, 7]
print(sorted(nums, key=lambda n: n % 10))

# 문제 4 - lambda로 두 번째 값 기준으로 정렬
data = [(1, 5), (2, 3), (3, 1)]
print(sorted(data, key=lambda x : x[1]))

# 문제 5 - lambda로 문자열 길이 내림차순 정렬
words = ["apple", "banana", "cat", "dog"]
print(sorted(words, key=lambda w : -len(w)))