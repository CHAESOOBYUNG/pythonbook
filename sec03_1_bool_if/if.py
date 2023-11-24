# if 조건문
## 조건이 True일 때만 들여쓰기 안쪽 문장 실행
## if 조건: 복합문장
## 복합문장: 문장을 묶어 놓은 것 (들여쓰기 사용)

# 예제 1
## 사용자가 입력한 숫자가 양수 음수 0인지 판별하는 프로그램
raw_input = input("정수를 입력해주세요: ")
raw_input = int(raw_input)

if raw_input > 0:
    print("양수입니다!")
if raw_input < 0:
    print("음수입니다!")
if raw_input == 0:
    print("0입니다!")
