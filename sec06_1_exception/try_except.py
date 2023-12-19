입력 = input("정수 입력> ")

try:
    숫자입력 = int(입력)
    print(f"원의 반지름: {숫자입력}")
    print(f"원의 둘레: {2 * 3.14 * 숫자입력}")
    print(f"원의 넓이: {3.14 * 숫자입력 * 숫자입력}")
except:
    print("숫자를 입력해주세요")

def isfloat(입력):
    try:
        float(입력)
        return True
    except:
        return False
    
입력리스트 = ["52", "273", "32.1", "103", "숫자로변환할수없는문자열"]
출력리스트 = []
for 요소 in 입력리스트:
    if isfloat(요소):
        출력리스트.append(float(요소))
print(출력리스트) # [52, 273, 32.1, 103]