# 캡슐화
# 객체를 사용하는 사람이 접근하지 못하게 하기위해
# 변수와 함수를 숨기는 작업
# 인스턴스 변수와 인스턴스 함수 앞에 __를 붙혀 만듬
class Circle:
    def __init__(self, 반지름):
        if 반지름 < 0:
            raise TypeError("반지름은 0 이상이어야 합니다.")
        self.__반지름 = 반지름 # 캡슐화
        self.__파이 = 3.14
    def 둘레(self):
        return 2 * self.__파이 * self.__반지름
    def 넓이(self):
        return self.__파이 * (self.__반지름 ** 2)
    # getter와 setter
    def get_반지름(self): # getter
        return self.__반지름
    def set_반지름(self, value): # setter
        if value < 0:
            raise TypeError("반지름은 0 이상이어야 합니다.")
        self.__반지름 = value

circle = Circle(10)
circle.__반지름 = -10 # 접근 불가
print(circle.get_반지름())
circle.set_반지름(20)
print(circle.둘레()) # 둘레를 구함
print(circle.넓이()) # 넓이를 구함