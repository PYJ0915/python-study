# 📚 Day 11 모의고사 핵심 정리

---

## ✅ 맞은 것들 핵심 정리

### Python 코드 해석

```python
# 슬라이싱
nums = [1, 2, 3, 4, 5]
nums[1:4]   # [2, 3, 4]
nums[::-1]  # [5, 4, 3, 2, 1]

# 다중 반환 + 언패킹
def calc(a, b):
    return a + b, a * b, a - b
x, y, z = calc(4, 2)   # 6 8 2

# 정렬 — 튜플 키 (길이 먼저, 같으면 알파벳 순)
sorted(words, key=lambda x: (len(x), x))
# ["kiwi", "apple", "mango", "banana"]

# 클래스 흐름 추적
c = Counter()
c.up()   # 1
c.up()   # 2
c.up()   # 3
c.down() # 2
c.value() # 2

# 리스트 펼치기 (flatten)
def flatten(lst):
    result = []
    for item in lst:
        if type(item) == list:
            result += item       # 리스트면 요소 추가
        else:
            result.append(item)  # 아니면 그대로 추가
    return result

flatten([1, [2, 3], 4, [5, 6]])  # [1, 2, 3, 4, 5, 6]

# 재귀 — 리스트 합계
def mystery(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + mystery(lst[1:])

mystery([1, 2, 3, 4, 5])  # 15
```

---

### Python 구현

```python
# 평균 이상인 값 추출
nums = [50, 70, 90, 40, 80]
avg = sum(nums) / len(nums)
[x for x in nums if x >= avg]   # [70, 90, 80]

# 피보나치
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# Stack 클래스
class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) == 0:
            print("비어있음")
        else:
            return self.data.pop()

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)

# BankAccount 클래스
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("잔액 부족")

    def get_balance(self):
        return self.balance
```

---

### SQL

```sql
-- GROUP BY + HAVING + ORDER BY
SELECT dept, COUNT(*) as cnt, AVG(age) as avg_age
FROM employee
GROUP BY dept
ORDER BY cnt DESC;

-- DELETE / TRUNCATE / DROP
DELETE FROM student WHERE id = 1;  -- 행 삭제, 복구 가능 (DML)
TRUNCATE TABLE student;            -- 전체 행 삭제, 복구 불가 (DDL)
DROP TABLE student;                -- 구조 + 데이터 삭제, 복구 불가 (DDL)

-- 서브쿼리 + IN
SELECT *
FROM student
WHERE dept IN (
    SELECT dept
    FROM student
    GROUP BY dept
    HAVING COUNT(*) >= 3   -- 인원 3명 이상인 부서에 속한 학생 전체 조회
);

-- LIKE 패턴 - 헷갈리는 패턴 정리
WHERE name LIKE '수%'    -- '수'로 시작
WHERE name LIKE '%수'    -- '수'로 끝
WHERE name LIKE '%수%'   -- '수'가 포함
WHERE name LIKE '수_'    -- '수'로 시작하는 2글자
WHERE name LIKE '_수'    -- '수'로 끝나는 2글자
WHERE name LIKE '김_'    -- '김'씨 외자 이름 (총 2글자)
WHERE name LIKE '김__'   -- '김'씨 두 글자 이름 (총 3글자)
```

---

### Linux

```bash
# 경로 계산
cd /home/user → mkdir project → cd project
→ mkdir src docs → cd src → cd ../docs
→ pwd: /home/user/project/docs

# 권한
chmod 700 test.txt   # rwx------ (소유자만 전체 권한)

# 폴더 복사
cp -r backup backup2   # -r 옵션 필요 (폴더 복사)

# ls -l 출력 해석
drwxr-xr-x → d = 폴더
-rw-r--r-- → - = 파일
```

---

### Java

```java
// 생성자 흐름 추적
B b = new B()
→ super(1)  → A(1) 호출
→ this()    → A() 호출  → "A" 출력
→ A(1)                  → "B1" 출력
→ B()                   → "C" 출력
결과: A B1 C

// 인터페이스 배열
Calc[] calcs = {new Add(), new Mul()};
for (Calc c : calcs) {
    System.out.println(c.run(3, 4));
}
// 7, 12

// static 변수
static int x = 10;
static void change() { x = 20; }
// 10 → 20
```

---

## ⚠️ 틀린 것들 핵심 정리

### 1. 대문자 추출 — isupper() 사용

```python
s = "Hello World Python"

# ❌ 각 단어 첫 글자만 추출 (조건에 따라 틀릴 수 있음)
[x[0] for x in s.split()]    # ['H', 'W', 'P']

# ✅ 대문자인 문자만 정확히 추출
[c for c in s if c.isupper()]  # ['H', 'W', 'P']

# 차이가 나는 경우
s = "hEllo wOrld"
[x[0] for x in s.split()]     # ['h', 'w'] ← 소문자도 포함
[c for c in s if c.isupper()]  # ['E', 'O'] ← 대문자만 정확히
```

---

### 2. JOIN + GROUP BY — 테이블명 명시 필수

```sql
-- ❌ 테이블명 없으면 어느 테이블 컬럼인지 모호함
SELECT name, SUM(amount)
FROM orders
JOIN users ON user_id = id
GROUP BY user_id

-- ✅ 테이블명 명시 + GROUP BY 에 SELECT 컬럼 포함
SELECT users.name, SUM(orders.amount)
FROM orders
JOIN users ON orders.user_id = users.id
GROUP BY users.id, users.name   -- SELECT 에 있는 컬럼 전부 포함
HAVING SUM(orders.amount) >= 1000
ORDER BY SUM(orders.amount) DESC
```

> 💡 GROUP BY 규칙
> SELECT 에 집계함수(SUM, COUNT 등)가 아닌 컬럼은
> 전부 GROUP BY 에 포함해야 해요

---

### 3. 서브쿼리 — 조회 범위 정확히 이해하기

```sql
SELECT *
FROM student
WHERE dept IN (
    SELECT dept FROM student
    GROUP BY dept
    HAVING COUNT(*) >= 3
);

-- 흐름
-- 1단계: 서브쿼리 → 인원 3명 이상인 dept 목록 추출
-- 2단계: 그 dept 에 속한 학생 전체 행 조회

-- ❌ 틀린 해석: 부서 목록만 조회
-- ✅ 맞는 해석: 해당 부서에 속한 학생 전체 정보 조회
```

---

## 📊 오늘 점수

| 파트 | 점수 |
|------|------|
| Python 해석 | 6 / 6 |
| Python 구현 | 3.5 / 4 |
| SQL | 3 / 4 |
| Linux | 3 / 3 |
| Java | 3 / 3 |
| **합계** | **18.5 / 20** |

---

## 🎯 시험 전 최종 체크리스트

```
Python
□ 재귀 — 종료 조건 먼저
□ 클래스 — self, __init__, 메서드
□ 슬라이싱 — s[::-1] 뒤집기
□ 컴프리헨션 — [x for x in lst if 조건]
□ Counter — most_common(), 동점은 실행해서 확인
□ 대문자 추출 — isupper() 사용

SQL
□ LIKE — % 글자수 제한 없음 / _ 한 글자
□ GROUP BY — SELECT 컬럼 전부 포함
□ JOIN — 테이블명.컬럼명 명시
□ 서브쿼리 — 조회 범위 정확히 파악
□ DELETE / TRUNCATE / DROP 차이

Linux
□ 경로 — ../ 개수만큼 뒤로
□ 권한 — r=4 w=2 x=1
□ cp -r — 폴더 복사 시 필수
□ mv — 이동 + 이름 변경 동시 가능

Java
□ == vs equals()
□ 메서드 오버라이딩 — 실제 객체 기준
□ 필드 — 선언 타입 기준
□ implements / extends 차이
□ 생성자 흐름 — this() / super() 순서 추적
```
