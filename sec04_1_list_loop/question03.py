numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    # 홀수 짝수
    if number % 2 == 0:
        print(f"{number}은/는 짝수입니다.")
    else:
        print(f"{number}은/는 홀수입니다.")

    # 자릿수 출력
    print(f"{number}은/는 {len(str(number))}자릿수입니다.")
    ## 숫자 -> 문자열 변환 후 길이 측정
    print()