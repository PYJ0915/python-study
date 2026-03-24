# 동적 프로그래밍 (DP) - 큰 문제를 작은문제로 쪼개서 작은 문제의 결과를 저장해두고 재활용하는 방법

# 1. DP를 사용하는 이유

# 피보나치를 통해 비교
# 일반 재귀 — O(2ⁿ) 매우 느림
def fib(n):
  if n <= 2: return 1
  return fib(n - 1) + fib(n - 2)

# fib(5) 호출 시
# fib(5)
# ├── fib(4)
# │   ├── fib(3)
# │   │   ├── fib(2) → 1
# │   │   └── fib(1) → 1
# │   └── fib(2) → 1
# └── fib(3)       ← fib(3) 중복 계산!
#     ├── fib(2) → 1
#     └── fib(1) → 1

# DP — O(n) 빠름
# 한 번 계산한 값을 저장해두고 재활용
# dp[1] = 1
# dp[2] = 1
# dp[3] = dp[2] + dp[1] = 2
# dp[4] = dp[3] + dp[2] = 3
# dp[5] = dp[4] + dp[3] = 5

# 2. DP 두 가지 방식
# 방식 1 - 메모이제이션 (하향식 Top-down)
# 재귀 + 캐시 저장
memo = {}
def fib(n):
  if n <= 2: return 1
  if n in memo: return memo[n]  # 이미 계산했으면 바로 반환
  memo[n] = fib(n - 1) + fib(n - 2) # 처음이면 계산 후 저장
  return memo[n]

print(fib(10))   # 55

# 방식 2 - 타뷸레이션 (상향식 Bottom-up) = 표(Table)를 채워나가는 방식
# 반복문으로 작은 것부터 채워나가기
def fib(n):
    dp = [0] * (n + 1)   # 표 만들기
    dp[1] = 1             # 초기값 설정
    dp[2] = 1             # 초기값 설정

    for i in range(3, n + 1):          # 작은 것부터
        dp[i] = dp[i-1] + dp[i-2]     # 표 채우기

    return dp[n]   # 원하는 값 꺼내기

print(fib(10)) # 55

# 3. 메모이제이션 VS 타뷸레이션

# 메모이제이션 — 하향식
# fib(10) 이 필요한 것만 계산
# fib(10)
#   → fib(9) 필요
#     → fib(8) 필요
#       ...

# 타뷸레이션 — 상향식
# fib(1)부터 fib(10)까지 전부 채움
# dp[1]=1 → dp[2]=1 → dp[3]=2 → ... → dp[10]=55

# 메모이제이션   → 위에서 아래로 (필요한 것만)
# 타뷸레이션     → 아래서 위로 (전부 채움)


# 4. DP 문제 푸는 공식 (타뷸레이션)
# 1) 점화식 찾기
#   → dp[i] 를 dp[i-1], dp[i-2] 등으로 표현

# 2) 초기값 설정
#   → dp[0], dp[1] 등 기저 케이스

# 3) 반복문으로 채우기
#   → 작은 것부터 큰 것 순서로

# 예제 1 - 계단 오르기
# 한 번에 1칸 또는 2칸 오를 수 있을 때 n번째 계단에 오르는 방법의 수

# 점화식 - dp[n] = dp[n-1] + dp[n-2]
#  → n번째 오는 방법 = (n-1번째에서 1칸) + (n-2번째에서 2칸)

def stairs(n: int) -> int:
  if n <= 2: return n

  dp = [0] * (n + 1)
  dp[1] = 1
  dp[2] = 2

  for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2]
  
  return dp[n]

print(stairs(5))   # 8
print(stairs(10))  # 89

# 예제 2 - 최대 부분합 (카데인 알고리즘)
# 연속된 부분 배열의 최대 합 구하기

# 점화식 - dp[i] = max(nums[i], dp[i-1], nums[i])
# → 현재 값 자체 vs 이전까지 합 + 현재 값
# → 이전 합이 마이너스면 현재부터 새로 시작

def max_subarray(nums: list) -> int:
    dp = [0] * len(nums)
    dp[0] = nums[0]        # 초기값

    for i in range(1, len(nums)):
        dp[i] = max(
            nums[i],           # 새로 시작
            dp[i-1] + nums[i]  # 이전 구간 연장
        )

    return max(dp)   # 전체 dp 중 최댓값

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(nums))   # 6

# 예제 3 - 배낭 문제 (Knapsack)
# 무게 제한이 있을 때 최대 가치 구하기

# 물건: [(무게, 가치)]
# items = [(2, 3), (3, 4), (4, 5), (5, 6)]
# 무게 제한: 8

def knapsack(items: list, capacity: int) -> int:
    n = len(items)

    # dp 테이블 생성
    # dp[i][w] = i번째 물건까지 고려했을 때, 무게 w 이하로 담을 수 있는 최대 가치
    # 행 = 물건 개수 (0 ~ n)
    # 열 = 무게 제한 (0 ~ capacity)
    # 초기값 0 = 물건 0개일 때는 가치 0
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        # items 는 0부터 시작하므로 i-1 로 접근
        weight, value = items[i-1]

        for w in range(capacity + 1):

            if weight > w:
                # 현재 물건 무게 > 현재 무게 제한
                # → 현재 물건 못 담음
                # → 이전 물건까지의 최대값 그대로 유지
                dp[i][w] = dp[i-1][w]

            else:
                # 현재 물건을 담을 수 있는 경우
                # 두 가지 선택지 중 더 큰 값 선택
                dp[i][w] = max(
                    dp[i-1][w],                  # 선택 1 — 현재 물건 안 담기
                                                 #          이전 물건까지의 최대값 유지

                    dp[i-1][w - weight] + value  # 선택 2 — 현재 물건 담기
                                                 # w - weight = 현재 물건 담고 남은 공간
                                                 # dp[i-1][w-weight] = 남은 공간에서 이전 물건들로 채울 수 있는 최대값
                                                 # + value = 현재 물건 가치 추가
                )

    # 전체 물건 고려 + 무게 capacity 이하일 때 최대 가치
    return dp[n][capacity]


# 예시
# items = [(무게2, 가치3), (무게3, 가치4), (무게4, 가치5), (무게5, 가치6)]
# capacity = 8
# 정답: 10 = (무게3, 가치4) + (무게5, 가치6)

items = [(2, 3), (3, 4), (4, 5), (5, 6)]
print(knapsack(items, 8))   # 10

#      w=0  w=1  w=2  w=3  w=4  w=5  w=6  w=7  w=8
# i=0:  0    0    0    0    0    0    0    0    0   ← 물건 0개
# i=1:  0    0    3    3    3    3    3    3    3   ← (무게2, 가치3) 고려
# i=2:  0    0    3    4    4    7    7    7    7   ← (무게3, 가치4) 고려
# i=3:  0    0    3    4    5    7    8    9    9   ← (무게4, 가치5) 고려
# i=4:  0    0    3    4    5    7    8    9   10   ← (무게5, 가치6) 고려
#                                               ↑
#                                            정답 10

# 예제 4 - 최장 공통 부분 수열 (LCS)
# 두 문자열의 공통 부분 수열 중 가장 긴 것
# s1 = "ABCBDAB"
# s2 = "BDCABA"
# → LCS = "BCBA" 길이 4

def lcs(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)

    # dp 테이블 생성
    # dp[i][j] = s1의 앞 i글자, s2의 앞 j글자까지 비교했을 때
    #            가장 긴 공통 부분 수열의 길이
    # 행 = s1 길이 (0 ~ m)
    # 열 = s2 길이 (0 ~ n)
    # 초기값 0 = 한쪽이 빈 문자열이면 공통 수열 없음
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if s1[i-1] == s2[j-1]:
                # 현재 비교하는 두 글자가 같은 경우
                # → 이전까지의 LCS + 1
                # → 대각선 위 값 + 1
                # 예) s1="ABC", s2="BAC" 에서 C가 같으면
                #     "AB" vs "BA" 의 LCS + 1
                dp[i][j] = dp[i-1][j-1] + 1

            else:
                # 현재 비교하는 두 글자가 다른 경우
                # → s1 한 글자 제외한 경우 vs s2 한 글자 제외한 경우
                #    둘 중 더 긴 LCS 선택
                # dp[i-1][j] = s1 에서 현재 글자 제외
                # dp[i][j-1] = s2 에서 현재 글자 제외
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # s1 전체, s2 전체 비교했을 때 LCS 길이
    return dp[m][n]


# 예시
# s1 = "ABCBDAB"
# s2 = "BDCABA"
# LCS = "BCBA" 또는 "BCAB" → 길이 4

print(lcs("ABCBDAB", "BDCABA"))   # 4

  #     ""  B  D  C  A  B  A
  # "":  0  0  0  0  0  0  0
  #  A:  0  0  0  0  1  1  1
  #  B:  0  1  1  1  1  2  2
  #  C:  0  1  1  2  2  2  2
  #  B:  0  1  1  2  2  3  3
  #  D:  0  1  2  2  2  3  3
  #  A:  0  1  2  2  3  3  4
  #  B:  0  1  2  2  3  4  4
  #                        ↑
  #                     정답 4

    
