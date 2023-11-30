A = "ctacaatgtcagtatacccattgcattagccgg"
카운터 = {}

for i in range(0, len(A), 3):
    a = A[i:i + 3]
    if len(a) != 3:
        continue
    if a not in 카운터:
        카운터[a] = 0
    카운터[a] += 1

print(카운터)
print(f"사용된 숫자의 종류는 {len(카운터)}개입니다.")
