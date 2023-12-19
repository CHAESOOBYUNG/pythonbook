"""
try:
    # 예외가 발생할 가능성이 있는 코드
    pass
except:
    # 예외가 발생했을 때 실행할 코드
    pass
else: # 거의 안씀
    # 예외가 발생하지 않았을 때 실행할 코드
    pass
finally: # 많이 사용
    # 무조건 실행하는 코드
    pass
"""
try:
    # 예외가 발생할 가능성이 있는 코드
    숫자입력 = int(input("정수 입력> "))
except:
    # 예외가 발생했을 때 실행할 코드
    print("정수를 입력하지 않았습니다.")
else:
    # 예외가 발생하지 않았을 때 실행할 코드
    print("원의 반지름: ", 숫자입력)
    print("원의 둘레: ", 2 * 3.14 * 숫자입력)
    print("원의 넓이: ", 3.14 * (숫자입력 ** 2))
finally:
     # 무조건 실행하는 코드
    print("무조건 실행되는 코드입니다.")

# try_except_finally 함수
def 함수():
    print("함수()에 진입했습니다.")
    try:
        print("try 구문에 진입했습니다.")
        return
        print("try 구문이 끝났습니다.")
    except:
        print("except 구문에 진입했습니다.")
    finally:
        print("finally 구문에 진입했습니다.")
    print("함수()가 끝났습니다.")
함수()
print()

# try_except_finally for문
for i in range(10):
    try:
        print("try 구문에 진입했습니다.")
        continue
        break
        print("try 구문이 끝났습니다.")
    except:
        print("except 구문에 진입했습니다.")
    finally:
        print("finally 구문에 진입했습니다.")
    print("for문이 끝났습니다.")