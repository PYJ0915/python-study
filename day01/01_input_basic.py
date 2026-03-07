n = int(input("입력할 숫자 개수 : "))

nums = []
for i in range(n) :
  x = int(input("숫자 입력 : "))
  nums.append(x)

print("합계 : ", sum(nums))
print("평균 : ", sum(nums) / len(nums))
print("최댓값 : ", max(nums))
print("최솟값 : ", min(nums))