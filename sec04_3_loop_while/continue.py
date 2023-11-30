# continue 키워드
# 현재 반복을 넘어갈 때 사용하는 구문
numbers = [5, 15, 6, 20, 7, 25]

for i in numbers:
    if i >= 10:
        print(i)
    
    if i < 10:
        continue