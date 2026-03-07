# 리스트 → 수정 가능
nums = [1, 2, 3]
nums[0] = 99

print(nums[0]) # 99

# 튜플 - 요소를 소괄호로 묶어 정의하는 순서가 있는 불변(Immutable) 시퀀스 자료형
# 튜플 → 수정 불가
t = (1, 2, 3)

# TypeError: 'tuple' object does not support item assignment
# t[0] = 99

print(t[0]) # 1

# 튜플 언패킹 (튜플을 변수에 한 번에 풀어서 담는 것)
t2 = (1, 5)

# 하나씩 꺼내는 것 가능
a = t2[0]
b = t2[1]

print("a :", a, " b :", b)

# 언패킹으로 한 줄에 가능
a, b = (4, 7)
print(a, b)

# 괄호 생략도 가능!
a, b = 3, 9
print(a, b)