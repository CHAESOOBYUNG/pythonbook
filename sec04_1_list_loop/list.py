a = [123, "abc", True]
print(a[0])
print(a[1])
print(a[2])
print(a[0:1])
print(a + a)
print(a * 5)
print(a[-1])
print(a[-2])
print(len(a))

# 리스트 반대로 돌리기
print(a[::-1])

# 중첩 리스트
b = [[1, 2, 3], [4, 5], [6, 7]]
b[0] # [1, 2, 3]
b[0][0] # 1

# 파괴적이다: 연산 후에 피연산자가 변형되는 것
c = 10
# = 할당 연산자
print(c) # c = 10
c = 20 # c의 값이 파괴 됨
print(c) # c = 20

# 비파괴적이다: 연산 후에도 피연산자가 변형되지 않는 것
d = 10
# +-*/ 연산자
print(d) # d = 10
e = d + 20  # d의 값을 파괴하지 못함
print(d) # d = 10
print(e)

# 아래 함수들은 대부분 파괴적
# 요소 추가: append(), insert(), extend()
f = [1, 2, 3, 4]
f.append(10) # 가장 마지막에 요소를 하나 추가
print(f)
f.insert(0, 20)  # 원하는 위치에 요소를 하나 추가
print(f)
f.extend([5, 6, 7, 8]) # f = f + [5, 6, 7, 8] # 가장 마지막에 요소를 여러 개 추가
print(f)

# 요소 제거: del, pop(), remove(), clear()
g = [1, 2, 3]
del g[0] # 제거하고 싶은 인덱스 입력
print(g) # [2, 3]
g.pop(0) # 제거하고 싶은 인덱스 입력(기본값 -1)
print(g) # [3]
g.remove(3) # 제거하고 싶은 요소를 입력
print(g) # []
g.clear() # 모든 요소를 제거
print(g) # []

# 요소 정렬: sort()
h = [52, 273, 1, 7, 9, 103, 58, 201]
h.sort()
print(h) # 오름차순으로 출력
h.sort(reverse=True)
print(h)

# 요소 존재를 확인: in, not in
print(52 in h) # True
print(0 in h) # False

print(52 not in h) # False
# print(not (52 in a))