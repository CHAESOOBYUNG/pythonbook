# 파일 처리
# 읽기 처리 / 쓰기 처리

# (1) 스트림 연결(stream)
# w 쓰기 모드, a 추가해서 쓰기 모드, r 읽기 모드
# 파일 = open("C:\\Users\\Chae Soobyung\\Desktop\\course\\pythonbook\\sec05_3_function_advanced\\test.txt", "r")

# (2) 스트림을 통해 데이터 통신
# 문자열 = 파일.read()
# print(문자열)

#(3) 스트림 해제
# 파일.close()

# r 읽기모드
with open("C:\\Users\\Chae Soobyung\\Desktop\\course\\pythonbook\\sec05_3_function_advanced\\test.txt", "r", encoding = "utf-8") as 파일:
    문자열 = 파일.read()
    print(문자열)

# w 쓰기 모드
with open("a.txt", "w", encoding = "utf-8") as 파일:
    파일.write("안녕하세요")

# a 추가해서 쓰기 모드
with open("a.txt", "a", encoding = "utf-8") as 파일:
    파일.write("안녕하세요")