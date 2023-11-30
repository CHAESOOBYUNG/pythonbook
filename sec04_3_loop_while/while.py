# while 반복문 > for 반복문
i = 0
while i < 10:
    # 복합 구문
    # 조건이 참이라면 반복
    print(f"{i}번째 반복입니다.")
    i += 1
print()

for i in range(0, 10):
    print(f"{i}번째 반복입니다.")

a = [1, 2, 1, 2]
value = 2

while value in a:
    a.remove(value)

print(a)