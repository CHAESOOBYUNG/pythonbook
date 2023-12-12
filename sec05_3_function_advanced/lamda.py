# 람다: 간단한 함수를 간단하게 해주는 문법
def power(숫자):
    return 숫자 ** 2

A = [1, 2, 3, 4, 5]

이터레이터 = map(power, A)
이터레이터 = map(lambda 숫자: 숫자 ** 2, A)
print(list(이터레이터))

이터레이터 = filter(lambda 숫자: 숫자 % 2 == 1, A)
print(list(이터레이터))