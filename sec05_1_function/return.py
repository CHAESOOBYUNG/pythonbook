def sum_all(start, end):
    # 항등원으로 초기화
    output = 0
    for i in range(start, end + 1):
        output += i
    return output

# sum_all() 함수
# 값을 계산하는 부분
# + 출력
# + 파일에 결과를 출력
# + 네트워크 통신으로 결과를 전송

print(sum_all(1, 10))
print(sum_all(1, 100))
sum_all(1, 1000)