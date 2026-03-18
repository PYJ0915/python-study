# 실습 문제
from typing import List, Dict
from collections import Counter
# 문제 1 - 아래 함수에 타입 힌트 추가
# 타입 힌트 추가 전
def filter_words(words, min_len):
    return [w for w in words if len(w) >= min_len]

# 타입 힌트 추가 후
# words: 문자열 리스트
# min_len: 정수
# 반환값: 문자열 리스트

def filter_words(words: List[str], min_len: int) -> List[str]:
    return [w for w in words if len(w) >= min_len]

# 문제 2 - 아래 조건으로 타입 힌트가 포함된 함수 구현
# - 함수명: word_count
# - 인자: 문자열 (str)
# - 반환값: 딕셔너리 (단어: 등장횟수)

def word_count(sentence: str) -> Dict[str, int]:
    return dict(Counter(sentence.split()))

print(word_count("hello world hello"))
# {'hello': 2, 'world': 1}

# 문제 3 - 터미널에서 직접 해보기
# 1. 새 폴더 만들고
# mkdir my_project
# cd my_project

# 2. 가상환경 만들고 활성화
# python -m venv venv
# source venv/bin/activate  # (Windows: venv\Scripts\activate)

# 3. requests 설치
# pip install requests

# 4. requirements.txt 저장
# pip freeze > requirements.txt

# 5. 내용 확인
# cat requirements.txt