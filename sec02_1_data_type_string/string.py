# 문자열 만들기 기본
# "안녕하세요"
# '안녕하세요'

# 문자열 안 문자열
# '"안녕하세요"라고 말했습니다'

# "": 문자열 리터럴
# 안녕하세요: 식별자
# "라고 말했습니다": 문자열 리터럴

## (1) 다른 따옴표 사용하기
# print('"안녕하세요"라고 말했습니다')

## (2) 이스케이프 문자 사용하기
# print("\"안녕하세요\"라고 말했습니다")

### \n 줄바꿈
# print("안녕\n하세요")

### \t 탭문자
# print("이름\t생년\t색상")
# print("원영\t04\t빨강")
# print("유진\t03\t자홍")
# print("리즈\t04\t청녹")
# print("이서\t07\t노랑")
# print("레이\t04\t초록")
# print("가을\t02\t파랑")

### \\ 역슬래시 자체
# print("\\ \\ \\ \\")

# 예제
print("동해물과 백두산이\n마르고 닳도록\n하느님이 보우하사\n우리나라 만세\n무궁화 삼천리 화려강산\n대한사람 대한으로\n길이 보전하세")
print("-=-==--=-=-")
print("""동해물과 백두산이 
마르고 닳도록
하느님이 보우하사 
우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 
길이 보전하세""")
print("-=-==--=-=-")
print("""\
동해 물과 백두산이 
마르고 닳도록
하느님이 보우하사 
우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 
길이 보전하세\
""")
print("-=-==--=-=-")

# 예제2
print\
(1, 2, 3) #print(1, 2, 3)