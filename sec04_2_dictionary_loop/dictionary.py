# 딕셔너리
# {}를 사용
# "키: 값" 쌍을 여러 개 입력
# 키: 숫자, 문자열, 불(, 튜플)
# 값: 모든 값
product = {
    "키": "값",
    "제품명": "건망고 슬라이스",
    "가격": 4000,
    "분류": "식품",
    "원산지": "태국",
    10: 20
}

print(product["제품명"]) # "건망고 슬라이스"
print(product["가격"]) # 4000
print(product["분류"]) # "식품"
print(product[10])
print()

# 반복문 적용
for key in product:
    print(key)
    print(product[key])
    print("-" * 20)
print()

# 딕셔너리, 리스트 혼합 -> 반복문 적용
products = [{
    "키": "값",
    "제품명": "건망고 슬라이스",
    "가격": 4000,
    "분류": "식품",
    "원산지": "태국",
    10: 20
}, {
    "키": "값",
    "제품명": "건망고 슬라이스",
    "가격": 4000,
    "분류": "식품",
    "원산지": "태국",
    10: 20
}]

for product in products:
    for key in product:
        print(key)
        print(product[key])
        print()
    print("-" * 20)