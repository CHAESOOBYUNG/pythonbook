class Circle:
    def __init__(self, 반지름):
        if 반지름 < 0:
            raise TypeError("반지름은 0 이상이어야 합니다.")
        self.__반지름 = 반지름 # 캡슐화
        self.__파이 = 3.14
    @property
    def 둘레(self):
        return 2 * self.__파이 * self.__반지름
    @property
    def 넓이(self):
        return self.__파이 * (self.__반지름 ** 2)
    @property
    def 반지름(self): # getter
        return self.__반지름
    @반지름.setter
    def 반지름(self, value): # setter
        if value < 0:
            raise TypeError("반지름은 0 이상이어야 합니다.")
        self.__반지름 = value

circle = Circle(10)
circle.반지름
circle.반지름 = 20
print(circle.둘레) # 둘레를 구함
print(circle.넓이) # 넓이를 구함