product = {
    "name": "7D 건조 망고",
    "type": "당절임"
}

# 요소의 값을 변경하는 방법
product["name"] = "8d 건조 망고"

# 요소를 추가하는 방법
product["price"] = 4000

# 요소를 제거하는 방법
del product["type"]

# 키의 존재를 확인하는 방법
# True or False
if "price" in product:
    print(product["price"])
else:
    print("아직 가격 요소가 없습니다.")

# get()
if product.get("price") != None:
    print(product["price"])
else:
    print("아직 가격 요소가 없습니다.")

print(product)