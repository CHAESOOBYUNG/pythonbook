# 등차수열
for n in range(1, 10 + 1):
    a_n = 2 * n - 1
    print(a_n) 
print()

# 1번째 항 ~ 10번째 항까지 들어있는 리스트
b = [0] # "없음"
for n in range(1, 10 + 1):
    b_n = 2 * n - 1
    b.append(b_n)
## a_1 = a[1] = 1
## a_2 = a[2] = 3
print()

# 점화식
c = [0]
for n in range(1, 10 + 1):
    if n == 1:
        c_n = 1
    else:
        c_n = c[n-1] + 2
    c.append(c_n)
print(c)
print()

# 동적계획법
N = 100
d = [0] * (N + 1)
for n in range(1, N + 1):
    if n == 1:
        d[1] = 1
    else:
        d[n] = d[n-1] + 2
print(d)
print()

# 피보나치 수열
N = 100
e = [0] * (N + 1)
for n in range(1, N + 1):
    if n == 1 or n == 2:
        e[n] = 1
    else:
        e[n] = e[n-1] + e[n-2]
print(e)

# 정수열 목록