# 방법 1
height = 10
for i in range(1, height + 1):
    result = ""
    result += " " * (height - i)
    result += "*" * (2 * i - 1)
    print(result)
print()

# 방법 2
height = 10
for i in range(1, height + 1):
    result=""
    for j in range(height - i):
        result += " "
    for j in range(2 * i - 1):
        result += "*"
    print(result)