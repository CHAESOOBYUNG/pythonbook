# for 반복문
# for 반복 변수 in 리스트: 
#   복합구문
a = [1, 2, 3, 4, 5]

# 반복 변수: a의 요소가 하나하나
# a의 요소가 무엇을 나타내는지 쉽게 이해할 수 있는 변수 이름
# i, j, k, m, n
for a_i in a:
    print(a_i)

# 총합
sum = 0 # 항등원
for a_i in a:
    sum = sum + a_i
print(sum)

# 총곱
prod = 1 # 항등원
for a_i in a:
    prod = prod * a_i
print(prod)