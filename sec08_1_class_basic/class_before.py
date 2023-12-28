def create_student(이름, 국어, 영어, 수학, 과학):
    return { "이름": 이름, "국어": 국어, "영어": 영어, "수학": 수학, "과학": 과학 }
def sum_student(학생):
    return 학생["국어"] + 학생["영어"] + 학생["수학"] + 학생["과학"]
def average_student(학생):
    return sum_student(학생) / 4

학생들 = [
    create_student("채수병", 87, 88, 98, 95),
    create_student("오타니", 92, 98, 97, 98),
    create_student("이정후", 76, 96, 95, 90)
]

# 문제(1) 합계를 구하는 함수가 있는지 + 평균을 구하는 함수가 있는지 자체를 모름
# 문제(2) "학생들"이라는 변수에 직접적으로 접근할 수 있음
# 문제(3) 함수가 분산되어 있음

print("이름", "총점", "평균", sep="\t")
for 학생 in 학생들:
    총점 = sum_student(학생)
    평균 = average_student(학생)
    print(학생["이름"], 총점, 평균, sep="\t")