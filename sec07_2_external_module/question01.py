from sympy import isprime

count = 0
for i in range(100, 1000 + 1):
    if isprime(i):
        count += 1

print(f"100~1000 사이에 있는 소수는 {count}개입니다.")