# 1~100 사이에 있는 숫자 중
# 2진법으로 변환했을 때
# 0이 하나만 포함된 숫자 
output = [
    i
    for i in range(1, 101)
    if f"{i:b}".count("0") == 1
]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))