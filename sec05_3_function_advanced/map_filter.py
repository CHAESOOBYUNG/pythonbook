# map()
# 각각의 요소에 함수를 적용해서
# 새로운 이터레이터를 리턴한다.
# 이터레이터 = map(함수, 리스트)
def power(숫자):
    return 숫자 ** 2

A = [1, 2, 3, 4, 5]
이터레이터 = map(power, A)
print(list(이터레이터)) # 강제 형변환
print([
    # 표현식
    숫자 ** 2
    # 반복문
    for 숫자 in range(1, 1 + 5)
])

# filter(함수, 리스트)
# 리스트의 요소를 함수에 전달했을 때
# 결과로 True가 나오는 요소를 모아서
# 새로운 이터레이터를 만듦
def 홀수인가요(숫자):
    if 숫자 % 2 == 1:
        return True
    else:
        return False
    
A = [1, 2, 3, 4, 5]
이터레이터 = filter(홀수인가요, A)
print(list(이터레이터)) # 강제 형변환
print([
    # 표현식
    숫자
    # 반복문
    for 숫자 in range(1, 5 + 1)
    # 조건문
    if 숫자 % 2 == 1
])
