# 클래스(설계도)
class Student:
    # 클래스의 내용
    # 기본 함수
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
    # (1) 비교연산자 함수
    def __eq__(self, 다른대상): # self == 다른대상
        if type(다른대상) == Student:
            return self.sum() == 다른대상.sum()
        elif type(다른대상) == int:
            return self.sum() == 다른대상
        else:
            raise "같은 자료형 또는 정수를 비교해주세요"
    def __ne__(self, 다른대상): # self != 다른대상
        if type(다른대상) == Student:
            return self.sum() != 다른대상.sum()
        elif type(다른대상) == int:
            return self.sum() != 다른대상
        else:
            raise "같은 자료형 또는 정수를 비교해주세요"
    def __gt__(self, 다른대상): # self > 다른대상
        if type(다른대상) == Student:
            return self.sum() > 다른대상.sum()
        elif type(다른대상) == int:
            return self.sum() > 다른대상
        else:
            raise "같은 자료형 또는 정수를 비교해주세요"
    def __ge__(self, 다른대상): # self >= 다른대상
        if type(다른대상) == Student:
            return self.sum() >= 다른대상.sum()
        elif type(다른대상) == int:
            return self.sum() >= 다른대상
        else:
            raise "같은 자료형 또는 정수를 비교해주세요"
    def __lt__(self, 다른대상): # self < 다른대상
        if type(다른대상) == Student:
            return self.sum() < 다른대상.sum()
        elif type(다른대상) == int:
            return self.sum() < 다른대상
        else:
            raise "같은 자료형 또는 정수를 비교해주세요"
    def __le__(self, 다른대상): # self <= 다른대상
        if type(다른대상) == Student:
            return self.sum() <= 다른대상.sum()
        elif type(다른대상) == int:
            return self.sum() <= 다른대상
        else:
            raise "같은 자료형 또는 정수를 비교해주세요"
    # (3) print() 함수를 일반적인 형태로 사용하는 함수
    def __str__(self):
        return f"{self.이름}\t{self.sum()}\t{self.average()}"   

class StudentList:
    # 기본함수
    def __init__(self):
        self.students = []
    def add(self, student):
        self.students.append(student)
    def print(self):
        print("이름", "총점", "평균", sep="\t")
        for student in self.students:
            student.print()
    # (2) + 연산자 함수
    def clone(self):
        output = StudentList()
        for student in self.students:
            output.add(student)
        return output
    def __add__(self, 다른대상): # self + 다른대상
        output = self.clone()
        output.add(다른대상)
        return output
    # (3) print() 함수를 일반적인 형태로 사용하는 함수
    def __str__(self):
        output = "이름\t총점\t평균\n"
        for student in self.students:
            output += f"{str(student)}\n"
        return output.strip()
    
    

# (1) 비교연산자 사용
a = Student("디그롬", 100, 100, 100, 100)
b = Student("슈어저", 100, 100, 100, 100)
print(a == b) # 두 학생의 성적 총합이 같을 경우 true
print(a > b)  # 두 학생의 성적 중에서 a가 더 클 때 true

# (2) + 연산자 사용
students = StudentList()
students += (Student("채수병", 87, 88, 98, 95))
students += (Student("오타니", 92, 98, 97, 98))
students.add(Student("이정후", 76, 96, 95, 90))
students.print()
print()

# (3) print() 함수를 일반적인 형태로 사용
print(Student("채수병", 87, 88, 98, 95))
print()
print(students)