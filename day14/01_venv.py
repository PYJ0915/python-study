# 가상환경 - 프로젝트마다 독립적인 파이썬 환경을 만드는 것
# 예시
# 프로젝트 A — Django 3.0 필요
# 프로젝트 B — Django 4.0 필요

# 가상환경 없이 → 둘 중 하나만 설치 가능 ❌
# 가상환경 있으면 → 각각 독립적으로 관리 ✅

# 1. venv - 가상환경 만들기
# 1) 가상환경 생성
# python -m venv venv

# 2) 가상환경 활성화
# source venv/bin/activate      # Mac / Linux
# venv\Scripts\activate         # Windows

# 3) 가상환경 비활성화
# deactivate

# 4) 가상환경 활성화 확인
# which python                  # Mac / Linux
# where python                  # Windows

# 2. pip - 패키지 관리
# 1) 패키지 설치
# pip install requests

# 2) 특정 버전 설치
# pip install requests==2.28.0

# 3) 패키지 삭제
# pip uninstall requests

# 4) 설치된 패키지 목록
# pip list

# 5) 패키지 정보
# pip show requests

# 6) 업그레이드
# pip install --upgrade requests

# 7) 현재 설치된 패키지 저장
# pip freeze > requirements.txt

# 8) requirements.txt 로 한 번에 설치
# pip install -r requirements.txt