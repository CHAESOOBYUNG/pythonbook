# reversed()
# 매개변수: 반복 가능한 것
# 결과: 그것을 뒤집은 것
# 결과 자료형: iterator
# -> list()를 사용해 리스트로 변환해서 결과 보기

# 리스트
print(list(reversed([1, 2, 3, 4, 5])))

# 범위
print(list(reversed(range(0, 10))))

for i in reversed(range(0, 10)):
    print(i)