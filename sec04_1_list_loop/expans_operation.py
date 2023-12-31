# 전개 연산자
# *리스트 = 요소, 요소, 요소
## (1) 리스트 내부
a = [1, 2, 3]
a.append(4)
print(a) # [1, 2, 3, 4]

a = [1, 2, 3]
b = [*a, 4] # [1, 2, 3, 4]
print("a: ", a)
print("b: ", b)

## (2) 함수의 매개변수 위치
date = [2023, 11, 21, 18, 18]

# "{}년 {}월 {}일 {}시 {}분".format(date[0],
# date[1], date[2], date[3], date[4]) 

print("{}년 {}월 {}일 {}시 {}분".format(*date))