# 📚 Day 09 학습 정리
> Linux → SQL → Java 복습 → 코드 해석

---

## 1️⃣ Linux 경로

```bash
# 절대경로 — 루트(/)부터 시작
/home/user/project

# 상대경로 — 현재 위치 기준
./folder      # 현재 폴더 안
../folder     # 한 단계 위
../../folder  # 두 단계 위
```

> 💡 경로 계산 공식
> `../`의 개수만큼 뒤로 가고 나머지 경로 붙이기
> 예) 현재: `/Users/user/workspace` + `../src/test` → `/Users/user/src/test`

---

## 2️⃣ Linux 핵심 명령어

```bash
pwd                    # 현재 위치 출력
ls / ls -l / ls -a     # 파일 목록 / 상세 / 숨김 포함

cd folder              # 폴더 이동
cd ..                  # 상위 폴더
cd ~                   # 홈 디렉토리

mkdir folder           # 폴더 생성
mkdir -p a/b/c         # 중간 폴더 포함 생성

rm file.txt            # 파일 삭제
rm -r folder           # 폴더 삭제
rm -f file.txt         # 강제 삭제

cp a.txt b.txt         # 파일 복사
cp a.txt .             # 현재 폴더로 복사 (. = 현재 폴더)
cp -r folder1 folder2  # 폴더 복사

mv a.txt folder/       # 파일 이동
mv a.txt b.txt         # 이름 변경 (이동 + 이름변경 동시 가능)

cat file.txt           # 파일 내용 출력
grep "hello" file.txt  # 문자열 검색
```

---

## 3️⃣ Linux 파일 권한

```bash
# 권한 구조
- rwx r-x r-x
│ │   │   └── other (다른 사용자)
│ │   └────── group (그룹)
│ └────────── user  (소유자)
└──────────── 파일종류 (- 파일 / d 폴더)

# 권한 숫자
r = 4 / w = 2 / x = 1 / - = 0

# 자주 쓰는 조합
chmod 755  # rwxr-xr-x
chmod 644  # rw-r--r--
chmod 777  # rwxrwxrwx
chmod 600  # rw-------

# 기호 표기법
chmod u+x file.txt   # user 실행 권한 추가
chmod g-w file.txt   # group 쓰기 권한 제거
chmod a+x file.txt   # 전체 실행 권한 추가

# u = user / g = group / o = other / a = all
# + = 추가 / - = 제거 / = = 설정
```

> ⚠️ 주의사항
> `rwxr-xr--` → 7 5 4 = 754
> `rwxr-x---` → 7 5 0 = 750 (other 권한 없을 때 0)

---

## 4️⃣ SQL 핵심 쿼리

```sql
-- 조회
SELECT name, age FROM student
WHERE age BETWEEN 20 AND 30
ORDER BY age DESC;

-- 패턴 검색 (LIKE)
WHERE name LIKE '박_'    -- 박씨 + 이름 1글자
WHERE name LIKE '김__'   -- 김씨 + 이름 2글자
WHERE name LIKE '%이'    -- 이로 끝나는
WHERE name LIKE '_이%'   -- 두 번째 글자가 이

-- % → 글자 수 제한 없음
-- _ → 딱 한 글자

-- 추가 / 수정 / 삭제
INSERT INTO student(name, age) VALUES('Tom', 20);
UPDATE student SET age = 21 WHERE name = 'Tom';
DELETE FROM student WHERE name = 'Tom';

-- 테이블 삭제 차이
DELETE FROM student;     -- 데이터만 삭제, 복구 가능
TRUNCATE TABLE student;  -- 데이터만 삭제, 복구 불가
DROP TABLE student;      -- 구조 + 데이터 전부 삭제
```

> ⚠️ 주의사항
> - `COUNT` = 개수 / `SUM` = 합계 혼동 주의
> - `컬럼` = 세로(열) / `행` = 가로(데이터 한 줄)

---

## 5️⃣ SQL JOIN / GROUP BY

```sql
-- INNER JOIN
SELECT users.name, orders.product
FROM users
JOIN orders
ON users.id = orders.user_id;

-- JOIN 종류
-- INNER JOIN → 교집합 (양쪽 다 있는 것)
-- LEFT JOIN  → 왼쪽 전부 (오른쪽 없으면 NULL)
-- RIGHT JOIN → 오른쪽 전부 (왼쪽 없으면 NULL)

-- GROUP BY + HAVING
SELECT user_id, COUNT(*)
FROM orders
GROUP BY user_id
HAVING COUNT(*) > 2;

-- WHERE vs HAVING
-- WHERE  → 그룹화 전 조건 (행 필터링)
-- HAVING → 그룹화 후 조건 (그룹 필터링)

-- 집계 함수
COUNT(*) / SUM(c2) / AVG(c2) / MAX(c2) / MIN(c2)
```

### NOT IN 예제 (예시 문제 11번)

| t1 c1 | t1 c2 | t2 c1 | t2 c2 |
|--------|--------|--------|--------|
| A | 5 | A | 3 |
| D | 2 | C | 7 |
| F | 3 | D | 6 |
| G | 1 | H | 2 |

```sql
SELECT SUM(c2) AS ans
FROM t2
WHERE c1 NOT IN (SELECT c1 FROM t1);
-- t1의 c1 → A, D, F, G 제외
-- t2에서 C(7), H(2) 남음
-- 결과: 9
```

---

## 6️⃣ Java 핵심 복습

```java
// 인터페이스
interface Op {
    int calc(int a, int b);
}
class Add implements Op {   // implements 키워드
    public int calc(int a, int b) {
        return a + b;
    }
}

// 상속
class Dog extends Animal {  // extends 키워드
    Dog() {
        super();            // 부모 생성자 호출
    }
}

// this vs super
this()   // 자기 자신 생성자 호출
super()  // 부모 생성자 호출

// 문자열 비교
t1 == t2        // 주소값 비교 ❌
t1.equals(t2)   // 값 비교 ✅
```

### 상속 흐름 추적 (예시 문제 8번)

```java
// Test1 t1 = new Test2('Z') 실행 시
// 1. Test2('Z') 호출
// 2. this() → Test2() 호출
// 3. super() → Test1() 호출 → "X" 출력
// 4. Test2() → "Y" 출력
// 5. Test2('Z') → "Z" 출력
// 결과: X Y Z
```

---

## ✅ 오늘 주의사항 모음

```
Linux
- mv 는 이동 + 이름변경 동시 가능
- cp 현재 폴더로 복사할 때 . 사용
- 경로 계산: ../개수만큼 뒤로 가기

SQL
- COUNT(개수) vs SUM(합계) 혼동 주의
- WHERE(그룹화 전) vs HAVING(그룹화 후)
- DELETE(복구가능) vs TRUNCATE(복구불가) vs DROP(구조삭제)
- LIKE: % = 글자수 제한없음 / _ = 딱 한글자

Java
- implements = 인터페이스 구현
- extends = 상속
- == 는 주소값 비교 / equals() 는 값 비교
```
