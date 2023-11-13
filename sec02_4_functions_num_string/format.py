a = 52
b = 273

# 52 + 273 = {더한 값}
print(a, "+", b, "=", a +  b)

# 52 + 273 = {더한 값}
# print(a + "+" + b + "=" + (a + b))
# c = str(a) + "+" + str(b) + "=" + str(a + b)
# print(c)

# format 예시
print("{}".format(10))
print("{} {}".format(10, 20))
print("{}년 {}월 {}일".format(2023, 11, 13))

## print(a + "+" + b + "=" + (a + b))
print("{} + {} = {}".format(a, b, a + b))

## c = str(a) + "+" + str(b) + "=" + str(a + b)
print("{}+{}={}".format(a, b, a + b))

## f-문자열
print(f"{a} + {b} = {a + b}")
print(f"""{a} + {b} = {a + b}
{a} - {b} = {a - b}
{a} * {b} = {a * b}
{a} / {b} = {a / b}""")