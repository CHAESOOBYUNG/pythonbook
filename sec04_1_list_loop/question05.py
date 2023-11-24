numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    # 정수 주기 반복: 나머지 연산
    # 1, 2, 3, 4, 5, 6, 7, 8, 9
    # a_n = 0, 1, 2, 0, 1, 2, 0, 1, 2
    output[(number&3) - 1].append(number)
    # number = 1 -> 1 % 3 = 1 - 1 = 0, 원하는 값: 0
    # number = 2 -> 2 % 3 = 2 - 1 = 1, 원하는 값: 1
    # number = 3 -> 3 % 3 = 0 - 1 = -1, 원하는 값: 2

print(output)