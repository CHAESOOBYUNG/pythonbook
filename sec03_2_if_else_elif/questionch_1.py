i = input("입력> ")

if "안녕" in i:
    print("> 안녕하세요.")
elif "몇 시" in i:
    from pytz import timezone
    from datetime import datetime
    today = datetime.now(timezone('Asia/Seoul'))
    print(f"지금은 {today.hour}시입니다.")
else:
    print(">", i)