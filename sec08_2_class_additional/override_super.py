# 오버라이드
class 부모:
    def 함수(self):
        print("부모의 함수입니다.")

class 자식(부모):
    def 함수(self):
        print("자식의 함수입니다.")
        # 1
        부모.함수(self)
        # 2 - 주로 사용
        super().함수()

child = 자식()
child.함수()

# 오버라이드/super()
class 버튼:
    def __init__(self):
        print("버튼을 초기화합니다.")
        print("버튼을 만듭니다.")
        print("버튼을 화면에 출력합니다.")

class 빨간버튼(버튼):
    def __init__(self):
        super().__init__()
        print("버튼을 빨간색으로 칠합니다.")

class 파란버튼(버튼):
    def __init__(self):
        super().__init__()
        print("버튼을 파란색으로 칠합니다.")

class 초록버튼(버튼):
    def __init__(self):
        super().__init__()
        print("버튼을 초록색으로 칠합니다.")

빨간버튼()
파란버튼()
초록버튼()