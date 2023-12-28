# 클래스: 함수(와 변수)를 묶어 놓은 것
# -> 객체를 만들어내기 위한 설계도

# 클래스(설계도)
class Student:
    # 클래스의 내용
    def __init__(self, 이름, 국어, 영어, 수학, 과학):
        self.이름 = 이름
        self.국어 = 국어
        self.영어 = 영어
        self.수학 = 수학
        self.과학 = 과학
    def sum(self):
        return self.국어 + self.영어 + self.수학 + self.과학
    def average(self):
        return self.sum() / 4
    def print(self):
        print(self.이름, self.sum(), self.average(), sep="\t")

class StudentList:
    def __init__(self):
        self.students = []
    def add(self, student):
        self.students.append(student)
    def print(self):
        print("이름", "총점", "평균", sep="\t")
        for student in self.students:
            student.print()

# 객체(인스턴스)
수병 = Student("수병", 87, 88, 98, 95)

# 함수 호출 방법 (1)
print(수병.이름, 수병.국어)

# 함수 호출 방법 (2)
print(수병.이름, 수병.국어)
수병.sum()
수병.average()
print()

students = StudentList()
students.add(Student("채수병", 87, 88, 98, 95))
students.add(Student("오타니", 92, 98, 97, 98)),
students.add(Student("이정후", 76, 96, 95, 90))

students.print()

# 스네이크 케이스: create_student -> 대부분
# 대문자 캐멀 케이스: CreateStudent -> 클래스