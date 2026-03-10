# 기능사 스타일 코드 해석

# 문제 1
def func(x, y=10):
    return x * y

print(func(3)) # 내 답 : 30
print(func(3, 4)) # 내 답 : 12

# 문제 2
nums = [1, 2, 3, 4, 5]

def mystery(lst):
    result = []
    for x in lst:
        if x % 2 == 0:
            result.append(x ** 2)
    return result

print(mystery(nums)) # 내 답 : [4, 16]

# 문제 3
def calc(a, b):
    return a + b, a * b, a - b

x, y, z = calc(4, 2)
print(x, y, z) # 내 답 : 6 8 2

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
print(c.value()) # 내 답 : 2

# 문제 5
def flatten(lst):
    result = []
    for item in lst:
        if type(item) == list:
            result += item
        else:
            result.append(item)
    return result

print(flatten([1, [2, 3], 4, [5, 6]])) # 내 답 : [1, 2, 3, 4, 5, 6]

# 핵심 정리
# 문제 5번 += vs append() 차이
# result = [1]
# result.append([2, 3])   # [1, [2, 3]] ← 리스트 자체가 추가
# result += [2, 3]        # [1, 2, 3]   ← 요소들이 추가
