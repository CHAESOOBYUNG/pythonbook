def mul(*values):
    output = 1
    for i in values:
        output *= i
    return output

# 함수를 호출합니다.
print(mul(5, 7, 9, 10))