# 사용자로부터 파일 이름을 입력 받고
# 그 파일의 내용을 int() 함수로 정수로 변환한 뒤 출력하는 프로그램
# 간소화 전
def 함수(파일이름):
    try:
        파일 = open(파일이름, "r")
        내용 = 파일.read()
        try:
            숫자 = int(내용)
            return 내용
        except:
            print("숫자로 변환할 수 없는 파일입니다.")
        finally:
            파일.close()
    except:
        print("존재하지 않는 파일입니다.")

파일이름 = input("파일 이름> ")
print(함수(파일이름))

# 간소화 후
def 함수(파일이름):
    파일 = None
    try:
        파일 = open(파일이름, "r")
        내용 = 파일.read()
        숫자 = int(내용)
        return 내용
    except FileNotFoundError:
        print("존재하지 않는 파일입니다.")
    except ValueError:
        print("숫자로 변환할 수 없는 파일입니다.")
    finally:
        if 파일 != None:
            파일.close()

파일이름 = input("파일 이름> ")
print(함수(파일이름))