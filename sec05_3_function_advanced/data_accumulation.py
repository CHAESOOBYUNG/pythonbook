파일경로 = "C:\\Users\\Chae Soobyung\\Desktop\\course\\pythonbook\\sec05_3_function_advanced\\data.txt"

# 파일 읽기
with open(파일경로, "r", encoding="utf-8") as 파일:
    데이터 = 파일.read()
    if 데이터 != "":
        print(데이터.strip().split("\n"))

# 데이터 입력 받기
문자열 = input("> 데이터를 입력해주세요: ")

# 파일 쓰기
with open(파일경로, "a", encoding="utf-8") as 파일:
    파일.write(문자열.strip() + "\n")