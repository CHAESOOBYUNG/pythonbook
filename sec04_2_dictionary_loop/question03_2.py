# 히스토그램
# 숫자는 무작위로 입력해도 상관 없습니다.
numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3] # 리스트
counter = {} # 딕셔너리

# (1) 요소의 출현을 확인하는 코드: 요소를 초기화
for number in numbers:
    if number not in counter:
        counter[number] = ""
# (2) 해당 요소의 빈도를 확인하는 코드
    counter[number] += "■"
# 최종 출력
for key in sorted(counter.keys()):
    print(f"{key}: {counter[key]}")
        
    