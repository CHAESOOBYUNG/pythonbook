A = [{
    "제목": "혼자 공부하는 파이썬",
    "가격": 18000
}, {
    "제목": "혼자 공부하는 머신러닝 + 딥러닝",
    "가격": 26000
}, {
    "제목": "혼자 공부하는 자바스크립트",
    "가격": 24000
}]

def 가격(요소):
    return 요소["가격"]

print(min(A, key=lambda 책: 책["가격"]))
print(max(A, key=lambda 책: 책["가격"]))

A.sort(key=lambda 책: 책["가격"])
print(A)