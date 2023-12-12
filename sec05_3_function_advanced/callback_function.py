# 함수는 변수에 저장할  수 있다.
# 매개변수로 전달되는 함수
def call_10_times(콜백함수):
    for i in range(10):
        콜백함수(i)

def print_hello(매개변수):
    print("안녕하세요", 매개변수)

# 매가변수를 함수로 입력해서 전달
call_10_times(print_hello)