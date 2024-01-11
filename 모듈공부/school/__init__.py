# __all__ = ["Student", "StudentList", "a"] # 모듈 캡슐화

from .student import Student # 상대경로
from .studentlist import StudentList # 상대경로

a = "모듈입니다."
def b():
    print("school 모듈입니다.")