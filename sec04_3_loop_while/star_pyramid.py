height = 10
for i in range(1, height + 1):
    print("*" * i)
print()

height2 = 10
for i in range(1, height2 + 1):
    result = ""
    for j in range(i):
        result += "*"
    print(result)
print()

# N개의 별을 가로 방향으로 출력하는 반복문
N = 10
for i in range(N):
    print("*", end = "")
print()