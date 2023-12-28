def 사각형넓이구하기(너비, 높이):
    if 너비 <= 0 or 높이 <= 0:
        raise ValueError("너비와 높이는 양수여야합니다.")
    return 너비 * 높이

print(사각형넓이구하기(0, -1))