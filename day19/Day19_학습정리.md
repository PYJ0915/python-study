# 📚 Day 19 파이썬 심화 — 동적 프로그래밍 (DP)

---

## 1️⃣ DP란?

### 핵심 개념

```
큰 문제를 작은 문제로 쪼개서
작은 문제의 결과를 저장해두고 재활용하는 방법

일반 재귀 → 같은 계산 중복 → O(2ⁿ) 느림
DP        → 한 번 계산 후 저장 → O(n) 빠름
```

### DP 문제 푸는 공식

```
1. 점화식 찾기   → dp[i] 를 이전 값으로 표현
2. 초기값 설정  → dp[0], dp[1] 등 기저 케이스
3. 반복문으로 채우기 → 작은 것부터 큰 것 순서로
```

---

## 2️⃣ 메모이제이션 vs 타뷸레이션

### 메모이제이션 (하향식 Top-down)

```python
# 재귀 + 캐시 저장
# 필요한 것만 계산

memo = {}   # 함수 밖에 선언 필수!

def fib_memo(n: int) -> int:
    if n <= 2: return 1
    if n in memo: return memo[n]    # 이미 계산했으면 바로 반환
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

# 또는 인자로 전달
def fib_memo(n: int, memo={}) -> int:
    if n <= 2: return 1
    if n in memo: return memo[n]
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
```

> ⚠️ memo 를 함수 안에 선언하면
> 재귀 호출마다 새로운 memo 생성 → 저장해도 재활용 불가

### 타뷸레이션 (상향식 Bottom-up)

```python
# 반복문으로 작은 것부터 채워나가기
# 전부 계산

def fib(n):
    dp = [0] * (n + 1)   # 1단계 — 표 만들기
    dp[1] = 1             # 2단계 — 초기값 설정
    dp[2] = 1

    for i in range(3, n + 1):          # 3단계 — 점화식으로 채우기
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# 표 채우는 과정
# 인덱스:  0  1  2  3  4  5  6   7   8   9  10
# dp:     [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### 비교

```
메모이제이션  → 위에서 아래로 (필요한 것만 계산)
타뷸레이션    → 아래서 위로  (전부 채움)
둘 다 시간복잡도 O(n) 으로 동일
```

---

## 3️⃣ 자주 나오는 DP 패턴

### 패턴 1 — 계단 오르기

```
한 번에 1칸 또는 2칸 오를 수 있을 때
n번째 계단에 오르는 방법의 수

점화식: dp[n] = dp[n-1] + dp[n-2]
```

```python
def stairs(n: int) -> int:
    if n <= 2: return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(stairs(5))    # 8
print(stairs(10))   # 89
```

---

### 패턴 2 — 최대 부분합 (카데인 알고리즘)

```
연속된 부분 배열의 최대 합

점화식: dp[i] = max(nums[i], dp[i-1] + nums[i])
       나 혼자 vs 이전까지 합 + 나 → 더 큰 값 선택

이전 합이 음수 → 버리고 새로 시작
이전 합이 양수 → 연장해서 더 큰 합 추구
```

```python
def max_subarray(nums: list) -> int:
    dp = [0] * len(nums)
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(
            nums[i],            # 새로 시작
            dp[i-1] + nums[i]   # 이전 구간 연장
        )

    return max(dp)

# 공간 최적화 버전
def max_subarray(nums: list) -> int:
    current = nums[0]
    best = nums[0]

    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        best = max(best, current)

    return best

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(nums))   # 6 ([4, -1, 2, 1])
```

---

### 패턴 3 — 배낭 문제 (Knapsack)

```
무게 제한 안에서 최대 가치 구하기 (물건 1번씩만 사용)

dp[i][w] = i번째 물건까지 고려 + 무게 w 이하 최대 가치

못 담으면   → dp[i-1][w]  이전 값 유지
담을 수 있으면 → max(안 담기, 담기)
담기 = dp[i-1][w - weight] + value
     = 남은 공간의 최대값 + 현재 가치
```

```python
def knapsack(items: list, capacity: int) -> int:
    n = len(items)
    # 초기값 0 = 물건 0개일 때 가치 0
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i-1]
        for w in range(capacity + 1):
            if weight > w:
                # 현재 물건 못 담음 → 이전 값 유지
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(
                    dp[i-1][w],                  # 안 담기
                    dp[i-1][w - weight] + value  # 담기
                )

    return dp[n][capacity]

items = [(2, 3), (3, 4), (4, 5), (5, 6)]
print(knapsack(items, 8))   # 10
```

---

### 패턴 4 — 동전 문제

```
최소 동전 개수로 target 만들기 (동전 1번씩만 사용)

배낭 문제와 동일한 구조
max → min / 가치 → 개수 로 바뀐 것

dp[i][t] = i번째 동전까지 고려 + 금액 t 만들 때 최소 개수

못 쓰면      → dp[i-1][t]  이전 값 유지
쓸 수 있으면 → min(안 쓰기, 쓰기)
쓰기 = dp[i-1][t - coin] + 1
```

```python
def coin_change(coins, target):
    n = len(coins)
    # inf 로 초기화 — 최솟값 구하니까 큰 값으로 시작
    dp = [[float('inf')] * (target + 1) for _ in range(n + 1)]

    # 금액 0은 동전 0개로 만들 수 있음
    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        coin = coins[i-1]
        for t in range(target + 1):
            if coin > t:
                dp[i][t] = dp[i-1][t]
            else:
                dp[i][t] = min(
                    dp[i-1][t],              # 안 쓰기
                    dp[i-1][t - coin] + 1    # 쓰기 (+1개)
                )

    result = dp[n][target]
    return result if result != float('inf') else -1

coins = [1, 5, 10, 25]
print(coin_change(coins, 36))   # 3 (25+10+1)
print(coin_change(coins, 11))   # 2 (10+1)
```

---

### 패턴 5 — LIS (최장 증가 부분 수열)

```
오름차순으로 증가하는 가장 긴 부분 수열

dp[i] = i번째 원소에서 끝나는 LIS 길이
초기값 = 1 (자기 자신만)

j < i 이고 nums[j] < nums[i] 이면
dp[i] = max(dp[i], dp[j] + 1)
```

```python
def lis(nums):
    n = len(nums)
    dp = [1] * n    # 초기값 1 (자기 자신)

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(lis([10, 9, 2, 5, 3, 7, 101, 18]))   # 4 (2,3,7,18)
print(lis([0, 1, 0, 3, 2, 3]))             # 4 (0,1,2,3)
```

---

### 패턴 6 — LCS (최장 공통 부분 수열)

```
두 문자열의 공통 부분 수열 중 가장 긴 것

dp[i][j] = s1의 앞 i글자, s2의 앞 j글자까지 비교했을 때 LCS 길이

같으면 → dp[i-1][j-1] + 1  (대각선 + 1)
다르면 → max(dp[i-1][j], dp[i][j-1])
```

```python
def lcs(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

print(lcs("ABCBDAB", "BDCABA"))   # 4
```

---

## ✅ 자주 나오는 DP 패턴 한눈에 비교

```
피보나치 / 계단  → dp[i] = dp[i-1] + dp[i-2]
최대 부분합      → dp[i] = max(nums[i], dp[i-1] + nums[i])
배낭 / 동전      → dp[i][w] = max or min (안 담기, 담기)
LIS             → dp[i] = max(dp[i], dp[j]+1) j < i
LCS             → 같으면 dp[i-1][j-1]+1 / 다르면 max
```

---

## ✅ 오늘 주의사항

```python
# 1. 메모이제이션 — memo 위치 주의
def fib(n, memo={}):   # ✅ 인자로 전달
    pass

memo = {}              # ✅ 함수 밖에 선언
def fib(n):
    pass

def fib(n):
    memo = {}          # ❌ 함수 안 선언 → 재귀마다 새로운 memo

# 2. 최솟값 구할 때 초기값
dp = [[float('inf')]...]   # 최솟값 → inf 로 초기화
dp = [[0]...]              # 최댓값 → 0 으로 초기화

# 3. 배낭 vs 동전
배낭 → max / 초기값 0   / 못 담으면 이전 유지
동전 → min / 초기값 inf / 금액 0은 항상 0개

# 4. LIS — 이중 반복문
for i in range(1, n):
    for j in range(i):    # j 는 i 보다 앞에 있는 모든 원소
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
```
