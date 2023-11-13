a = "abcdabcd"

# find(): 왼쪽부터 탐색 / 1 출력
print(a.find("b"))
# rfind(): 오른쪽부터 탐색 / 5 출력
print(a.rfind("b"))

# 없는 문자 탐색 / -1 출력
print(a.find("z"))

# in 연산자
print("안녕" in "안녕하세요")
print("잘가" in "안녕하세요")

# format04, 05, 06 참고