# 실습 문제

# 문제 1 - 동전 문제 — 최소 동전 개수로 target 만들기
def coin_change(coins, target):
    n = len(coins)

    # float('inf') 로 초기화 — 최솟값 구하니까 큰 값으로 시작
    dp = [[float('inf')] * (target + 1) for _ in range(n + 1)]

    # 금액 0은 동전 0개로 만들 수 있음
    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        coin = coins[i-1]
        for t in range(target + 1):

            if coin > t:
                # 현재 동전 못 씀 → 이전까지 최솟값 유지
                dp[i][t] = dp[i-1][t]
            else:
                dp[i][t] = min(
                    dp[i-1][t],              # 현재 동전 안 쓰기
                    dp[i-1][t - coin] + 1    # 현재 동전 쓰기 (+1개)
                )

    result = dp[n][target]
    return result if result != float('inf') else -1

coins = [1, 5, 10, 25]
print(coin_change(coins, 36))   # 3 (25+10+1)
print(coin_change(coins, 11))   # 2 (10+1)

# 표로 확인
# coins = [1, 5, 10, 25], target = 11

#       t=0  t=1  t=2  ...  t=10  t=11
# i=0:   0   inf  inf  ...  inf   inf
# i=1:   0    1    2   ...  10    11    ← 동전1 사용
# i=2:   0    1    2   ...   2     3    ← 동전5 사용
# i=3:   0    1    2   ...   1     2    ← 동전10 사용 ← 10+1=2개 ✅
# i=4:   0    1    2   ...   1     2    ← 동전25 사용불가


# 문제 2 - 최장 증가 부분 수열 (LIS) — 오름차순으로 증가하는 가장 긴 부분 수열
def lis(nums):
    n = len(nums)

    # dp[i] = i번째 원소에서 끝나는 LIS 길이
    # 자기 자신만 있어도 길이 1
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            # j가 i보다 앞에 있고 값이 작으면
            # j에서 끝나는 LIS 에 i를 추가할 수 있음
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)   # 전체 dp 중 최댓값

print(lis([10, 9, 2, 5, 3, 7, 101, 18]))   # 4
print(lis([0, 1, 0, 3, 2, 3]))             # 4


# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# index=   0  1  2  3  4  5   6   7

# dp 초기값 = [1, 1, 1, 1, 1, 1, 1, 1]

# i=1 (9):  9<10? No  → dp[1] = 1
# i=2 (2):  2<10? No  → dp[2] = 1
#           2<9?  No  → dp[2] = 1
# i=3 (5):  5<10? No
#           5<9?  No
#           5<2?  No  → dp[3] = 1
#           5>2!  → dp[3] = max(1, dp[2]+1) = 2
# i=4 (3):  3>2   → dp[4] = max(1, dp[2]+1) = 2
# i=5 (7):  7>2   → dp[5] = max(1, dp[2]+1) = 2
#           7>5   → dp[5] = max(2, dp[3]+1) = 3
#           7>3   → dp[5] = max(3, dp[4]+1) = 3
# i=6 (101): 101>전부 → dp[6] = max(..., dp[5]+1) = 4
# i=7 (18):  18>7  → dp[7] = max(..., dp[5]+1) = 4

# dp = [1, 1, 1, 2, 2, 3, 4, 4]
# max(dp) = 4 ✅


# 두 문제 핵심 패턴 비교

# 동전 문제 → 배낭형 (2차원 dp)
#            dp[i][t] = min(안쓰기, 쓰기)
#            초기값 → inf (최솟값 구하니까)

# LIS      → 1차원 dp
#            dp[i] = i에서 끝나는 최장 길이
#            이전 원소들과 전부 비교
#            초기값 → 1 (자기 자신만)


# 문제 3 - 메모이제이션으로 피보나치 구현
def fib_memo(n: int) -> int:
  memo = {}    # ❌ 함수 안에 memo 선언 - memo 가 함수 안에 있으면 재귀 호출할 때마다 새로운 memo 가 생김
  if n <= 2: return 1
  if n in memo: return memo[n]
  memo[n] = fib_memo(n-1) + fib_memo(n-2)
  return memo[n]

print(fib_memo(10))   # 55
print(fib_memo(30))   # 832040


# 문제 3번 개선 풀이
# 방법 1 — memo 를 함수 밖에 선언
memo = {}

def fib_memo(n: int) -> int:
    if n <= 2: return 1
    if n in memo: return memo[n]
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

# 방법 2 — memo 를 인자로 전달 (더 깔끔)
def fib_memo(n: int, memo={}) -> int:
    if n <= 2: return 1
    if n in memo: return memo[n]
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]