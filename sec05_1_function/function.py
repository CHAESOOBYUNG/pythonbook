# 매개변수: 함수의 괄호 안에 넣는 변수

## parameter: 함수 정의 때 넣은 변수
## 함수를 설계하는 사람
## 1. 함수의 설명서 -> 문서(documentation)
## 2. 예외처리
def print_3_times(문자열, 횟수): # 함수
    # 예외처리
    if type(문자열) != str:
        print("첫 번째 매개변수는 문자열을 입력해야 합니다!")
    if type(횟수) != int:
        print("두 번째 매개변수는 정수를 입력해야 합니다!")
    
    for i in range(횟수):
        print(문자열)

## argument: 함수 호출 때 넣은 값
## 함수를 사용하는 사람
print_3_times("안녕", 3)