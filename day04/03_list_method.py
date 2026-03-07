# append(x) — x를 리스트 맨 뒤에 추가
nums = [1,2,3]
nums.append(4)
print(nums) # [1, 2, 3, 4]

# insert(index, x) — index 위치에 x 삽입
nums = [1,2,3]
nums.insert(1,5)
print(nums) # [1,5,2,3]

# pop() — 마지막 값 제거 후 반환
nums = [1,2,3]
nums.pop()
print(nums) # [1,2]
# 특정 위치 제거도 가능
nums = [1,2,3]
nums.pop(1)
print(nums) # [1,3]

# remove() — 특정값 제거
nums = [1,2,3,2]
nums.remove(2)
print(nums)

# index(x) — x의 인덱스 반환
nums = [10,20,30]
print(nums.index(20)) # 1

# count(x) — x의 개수 세기
nums = [1,2,2,3]
print(nums.count(2)) # 2

# sort() — 리스트 정렬
nums = [3,1,2]
nums.sort()
print(nums) # [1, 2, 3]

# sorted() — 정렬된 새 리스트
nums = [3,1,2]
print(sorted(nums)) # [1, 2, 3]

# reverse() — 뒤집기
nums = [1,2,3]
nums.reverse()
print(nums) # [3, 2, 1]

# extend(list2) — 리스트 합치기
a = [1,2]
b = [3,4]
a.extend(b)
print(a) # [1, 2, 3, 4]