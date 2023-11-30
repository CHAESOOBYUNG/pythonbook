# 리스트 내포(list_comprehension)
# 반복 가능한 것을 기반으로 
# 새로운 리스트를 만들어내는 문법

# A = []
# for i in range(0, 10):
#     A.append(2 * i + 1)
# print(A)
A = [
    2 * i + 1               # 표현식
    for i in range(0, 10)   # 조건문
]

# B = []
# for i in range(0, 10): 
#     if i % 2 == 0:
#         B.append(2 * i + 1)
# print(B)
B = [
    2 * i + 1               # 표현식
    for i in range(0, 10)   # 조건문
    if i % 2 ==0            # 반복문
]

print(A)
print(B)