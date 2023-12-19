# 가독성 상승 -> 유지보수성 상승
파이 = 3.141592

# 유지보수
def 숫자입력():
    number_input_a = input("> 숫자입력:")
    return float(number_input_a)

def 둘레구하기(radius):
    return 2 * 파이 * radius

def 넓이구하기(radius):
    return 파이 * radius * radius

반지름 = 숫자입력()
print(둘레구하기(반지름))
print(넓이구하기(반지름))

def p(문자열):
    return "<p class='content-line'>{}</p>".format(문자열)

print(p("안녕하세요"))
print(p("간단한 HTML 태그입니다."))