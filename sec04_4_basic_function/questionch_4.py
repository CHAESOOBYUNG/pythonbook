A = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
B = []

for a in A:
    if type(a) == list:
        for i in a:
            B.append(i)
            # B += [i]
    else:
        B.append(a)
        # B += [a]

print(f"{A}를 평탄화하면")
print(f"{B}입니다.")