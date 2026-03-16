# 1️⃣ Python 코드 해석 (6문제)
# 문제 1
nums = [1, 2, 3, 4, 5]
print(nums[1:4]) # 내 답: [2, 3, 4]
print(nums[::-1]) # 내 답: [5, 4, 3, 2, 1]

# 문제 2
def calc(a, b):
    return a + b, a * b, a - b

x, y, z = calc(4, 2)
print(x, y, z) # 내 답: 6 8 2

# 문제 3
words = ["banana", "apple", "kiwi", "mango"]
result = sorted(words, key=lambda x: (len(x), x))
print(result) # 내 답: ["kiwi", "apple", "mango", "banana"]

# 문제 4
class Counter:
    def __init__(self):
        self.count = 0

    def up(self):
        self.count += 1

    def down(self):
        self.count -= 1

    def value(self):
        return self.count

c = Counter()
c.up()
c.up()
c.up()
c.down()
print(c.value()) # 내 답: 2

# 문제 5
def flatten(lst):
    result = []
    for item in lst:
        if type(item) == list:
            result += item
        else:
            result.append(item)
    return result

print(flatten([1, [2, 3], 4, [5, 6]])) # 내 답: [1, 2, 3, 4, 5, 6]

# 문제 6
def mystery(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + mystery(lst[1:])

print(mystery([1, 2, 3, 4, 5])) # 내 답: 15

# 2️⃣ Python 구현 문제 (4문제)
# 문제 7 - 숫자 리스트에서 평균 이상인 값만 추출
nums = [50, 70, 90, 40, 80]
# 결과: [70, 90, 80]

print([x for x in nums if x >= sum(nums) / len(nums)])

# 문제 8 - 문자열에서 대문자만 추출해서 리스트로 반환
s = "Hello World Python"
# 결과: ['H', 'W', 'P']
print([x[0] for x in s.split()])

# 문제 9 - 아래 조건으로 함수 구현
# - 단어 리스트를 입력받아
# - 길이가 4 이상인 단어만
# - 길이 내림차순으로 정렬해서 반환

# 입력: ["hi", "apple", "cat", "banana", "ok"]
# 결과: ["banana", "apple"]
def fn(lst):
  return sorted([x for x in lst if len(x) >= 4], reverse=True, key=len)

word_list = input("입력 :").split()
print(fn(word_list))

# 문제 10 - 아래 조건으로 클래스 구현
# 클래스명: BankAccount
# 속성: balance (초기값 0)
# 메서드:
#     deposit(amount)   → 입금 (balance 증가)
#     withdraw(amount)  → 출금 (balance 감소, 잔액 부족하면 "잔액 부족" 출력)
#     get_balance()     → 현재 잔액 반환

class BankAccount:
  def __init__(self):
    self.balance = 0
    
  def deposit(self, amount):
     self.balance += amount
    
  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
    else :
      print("잔액 부족")

  def get_balance(self):
     return self.balance

acc = BankAccount()
acc.deposit(1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance())   # 1200
acc.withdraw(2000)         # 잔액 부족

