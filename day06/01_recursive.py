# 재귀함수 - 함수 내부에서 자기 자신을 다시 호출하여 문제를 더 작은 단위로 분할해 해결하는 프로그래밍 기법

# 예시
def f(n) :
  if n == 0 :
    return 0
  return n + f(n-1)

# 핵심 - 종료 조건이 반드시 있어야 함!

# ❌ 종료 조건 없음 → 무한 루프
# def f(n) :
#   return n + f(n-1)

# ✅ 종료 조건 있음
def f(n):
    if n == 0:
        return 0
    return n + f(n-1)

# 흐름 추적 - f(3)
# f(3)
# → 3 + f(2)
# → 3 + 2 + f(1)
# → 3 + 2 + 1 + f(0)
# → 3 + 2 + 1 + 0
# → 6
print(f(3))

# 연습 문제
# 문제 1 - 팩토리얼
def fac(n) :
   if n == 1 :
      return 1
   return n * fac(n-1)

print(fac(5))

# 문제 2 - 재귀로 리스트 합계
nums = [1, 2, 3, 4, 5]
def list_sum(nums) :
   if len(nums) == 0 :
      return 0
   return nums[0] + list_sum(nums[1:])

print(list_sum(nums))

# 문제 3 - 피보나치
def fi(n) :
   if n == 1 :
    return 1
   if n == 2 :
    return 1
   return fi(n-1) + fi(n-2)
   
print(fi(6))
