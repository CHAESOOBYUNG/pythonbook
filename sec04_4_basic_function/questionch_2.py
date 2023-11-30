A = "ctacaatgtcagtatacccattgcattagccgg"
카운터 = {}

for i in A:
    if i not in 카운터:
        카운터[i] = 0
    카운터[i] += 1

print(f"염기 서열을 입력해주세요: {A}")
print(카운터)
print("a의 개수: " + str(카운터['a']))
print("t의 개수: " + str(카운터['t']))
print("g의 개수: " + str(카운터['g']))
print("c의 개수: " + str(카운터['c']))