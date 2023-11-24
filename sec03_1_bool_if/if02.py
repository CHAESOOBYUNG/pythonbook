# 예제 2
## 오전 오후 구분하는 프로그램
## python datetime timezone 검색
from pytz import timezone
from datetime import datetime
today = datetime.now(timezone('Asia/Seoul'))

print(f"{today.hour}시입니다.")

if today.hour < 12:
    print("오전입니다.")

if today.hour >= 12:
    print("오후입니다.")

# 예제 2
## 계절을 구분하는 프로그램

m = today.month

if 3 <= m <=5:
    print("봄입니다.")

if 6 <= m <= 8:
    print("여름입니다.")

if 9 <= m <= 10:
    print("가을입니다.")

if(11 <= m <= 12) or (m == 1):
    print("겨울입니다.")