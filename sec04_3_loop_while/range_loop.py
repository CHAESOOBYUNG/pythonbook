# 범위
# 특정한 범위 내부의 정수들을 나열하는 자료형

# (1) range(A)
# 0부터 A까지의 정수를 범위로 나열
# A는 포함하지 않음

# (2) range(A, B)
# A부터 B까지의 정수를 범위로 나열
# B는 포함하지 않음

# (3) range(A, B, C)
# A부터 B까지의 정수를 범위로 나열
# B는 포함하지 않음
# C만큼씩 건너뛰면서 범위를 생성

# 예제
for i in range(10):
    print(f"{i}번째입니다")
print()

for _ in range(10):
    print(f"{_}번째입니다")
print()

# 끝자리 포함 강조
for i in range(0, 10 + 1):
    print(f"{i}번째입니다")
print()

# 1개 넣는 경우: 특정 횟수만큼 반복하는 경우
for i in range(10):
    print("반복입니다")
print()

# 2개 넣는 경우: 반복 변수를 사용하는 경우
for i in range(0, 10):
    print(f"{i}번째입니다")
print()

# 3개 넣는 경우: 반대로 반복하는 경우
for i in range(10, -1, -1):
    print(f"{i}번째입니다")