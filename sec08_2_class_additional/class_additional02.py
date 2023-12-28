# 값 객체
class CmLength:
    def __init__(self, cm):
        if cm < 0:
            raise ValueError("길이는 0 이상으로 지정해야 합니다.")
        self.__length = cm

    def get(self):
        return self.__length

    def __add__(self, 다른대상):
        if type(다른대상) != CmLength:
            raise TypeError("길이 단위를 통일해주세요!")
        return CmLength(self.get() + 다른대상.get())

result = CmLength(3) + CmLength(10)
print(result.get())  # 결과 출력