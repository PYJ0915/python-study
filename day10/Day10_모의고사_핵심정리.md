# 📚 Day 10 모의고사 핵심 정리

---

## ✅ 맞은 것들 핵심 정리

### Python

```python
# 재귀 — 팩토리얼
def mystery(n):
    if n == 1:
        return 1
    return n * mystery(n-1)

mystery(5)  # 5 * 4 * 3 * 2 * 1 = 120

# filter + map 조합
nums = [1, 2, 3, 4, 5]
list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
# filter → 짝수만 [2, 4]
# map   → 제곱    [4, 16]

# 클래스 상속 — 메서드 오버라이딩
class Animal:
    def speak(self):
        return f"{self.name} 소리를 냅니다"

class Dog(Animal):
    def speak(self):                    # 오버라이딩
        return f"{self.name}: 왈왈!"

# 딕셔너리 컴프리헨션 + 조건
{k: v for k, v in d.items() if v % 2 == 0}

# 기본값 인자
def func(lst, target=0):
    return [x for x in lst if x > target]

func(nums)      # target = 0 기본값 사용
func(nums, 3)   # target = 3 으로 덮어씀

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
        return self.data[-1]       # -1 인덱스로 마지막 접근

    def size(self):
        return len(self.data)

# 공통 요소 추출 — set 교집합
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
sorted(set(a) & set(b))   # [3, 4, 5]
```

---

### SQL

```sql
-- GROUP BY + HAVING
SELECT dept, AVG(score) as avg_score
FROM student
GROUP BY dept
HAVING AVG(score) >= 90
ORDER BY avg_score DESC;

-- LIKE 패턴
WHERE name LIKE '김_'     -- 김씨 + 외자 (총 2글자)
WHERE name LIKE '김__'    -- 김씨 + 이름 2글자 (총 3글자)

-- DELETE / TRUNCATE / DROP 차이
DELETE FROM student WHERE id = 1;  -- 행 삭제, 복구 가능 (DML)
TRUNCATE TABLE student;            -- 전체 행 삭제, 복구 불가 (DDL)
DROP TABLE student;                -- 구조 + 데이터 삭제, 복구 불가 (DDL)
```

---

### Linux

```bash
# 경로 계산
현재 위치: /home/user/project/src
cd ../../docs
→ src → project → /home/user/docs

# 권한
-rwxr-x--- = 750
rwx = 7 / r-x = 5 / --- = 0

# 파일 복사 + 이름 변경 동시에
cp a.txt /home/user/backup/a_backup.txt
```

---

### Java

```java
// new String() vs 리터럴
String a = new String("hello");
String b = new String("hello");
String c = "hello";
String d = "hello";

a == b        // false (new → 다른 주소)
a.equals(b)   // true  (값 비교)
c == d        // true  (리터럴 → 같은 상수 풀)
c.equals(d)   // true  (값 비교)

// 인터페이스
interface Shape {
    double area();
}
class Circle implements Shape {
    double r;
    Circle(double r) { this.r = r; }
    public double area() { return 3.14 * r * r; }
}
Shape s = new Circle(5);
s.area();   // 78.5
```

---

## ⚠️ 틀린 것들 핵심 정리

### 1. 함수 인자는 매개변수로 받기

```python
# ❌ input() 으로 받으면 안 됨
def char_freq():
    s = input("문자열 입력: ")
    return Counter(s.replace(" ", "")).most_common()

# ✅ 매개변수로 받기
def char_freq(s):
    return Counter(s.replace(" ", "")).most_common()

char_freq("hello world")
```

### 2. ORDER BY 뒤에 컬럼명 필수

```sql
-- ❌ 컬럼명 없음
ORDER BY DESC

-- ✅ 컬럼명 필수
ORDER BY score DESC
ORDER BY avg_score DESC
```

### 3. Java 필드는 오버라이딩 안 됨

```java
class Parent {
    int x = 10;
    void print() { System.out.println("Parent: " + x); }
}
class Child extends Parent {
    int x = 20;
    void print() { System.out.println("Child: " + x); }
}

Parent p = new Child();
p.print();             // "Child: 20" ← 메서드는 실제 객체(Child) 기준
System.out.println(p.x);  // 10 ← 필드는 선언 타입(Parent) 기준

// 메서드 → 오버라이딩 O → 실제 객체 타입 기준
// 필드   → 오버라이딩 X → 선언 타입 기준
```

### 4. Java 접근 제어자 없으면 직접 접근 가능

```java
class Parent {
    private int x = 10;  // ❌ 외부 접근 불가 → getter 필요
    public int x = 10;   // ✅ 외부 접근 가능
    int x = 10;          // ✅ 같은 패키지면 접근 가능 (default)
}

// 기능사 시험은 접근 제어자 생략 케이스 자주 나옴
// → p.x 직접 접근 가능
```

---

## 📊 오늘 점수

| 파트 | 점수 |
|------|------|
| Python 해석 | 6 / 6 |
| Python 구현 | 3.5 / 4 |
| SQL | 3 / 4 |
| Linux | 2.5 / 3 |
| Java | 2.5 / 3 |
| **합계** | **17.5 / 20** |
