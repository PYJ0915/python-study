n = int(input("입력할 숫자 개수 : "))

nums = []
for i in range(n) :
  x = int(input("숫자 입력 : "))
  nums.append(x)

# 1. 홀수 개수 구하기
oddCount = 0
for x in nums :
  if x % 2 != 0 :
    oddCount += 1

print("홀수의 개수 : ", oddCount)

# 2. 3의 배수의 합 구하기
total = 0
for x in nums :
  if x % 3 == 0 :
    total += x

print("3의 배수 합계 : ", total)

# 3. 음수 개수 구하기
minusCount = 0
for x in nums :
  if x < 0 :
    minusCount += 1

print("음수의 개수 : ", minusCount)

# 4. 가장 큰 짝수 구하기
max_even = None
for x in nums :
  if x % 2 == 0 :
    if max_even is None or x > max_even:
      max_even = x

print("가장 큰 짝수 : ", max_even)
    

# 5. 평균 이상인 값 개수 구하기
avgOvers = []
avg = (sum(nums) / len(nums))

for x in nums :
  if x >= avg :
    avgOvers.append(x)

print("평균 : ", avg)
print("평균 이상인 값의 개수 : ", len(avgOvers))