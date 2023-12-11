# 피보나치 수열
# 느린 함수
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return f(n - 1) + f(n - 2)
    
print(f(35))

# 빠른 함수
memo = { 1: 1, 2: 1 }
def f(n):
    # 조기 리턴 패턴
    if n in memo:
        return memo[n]
    else:
        temp = f(n - 1) + f(n - 2)
        memo[n] = temp
        return temp

print(f(50))