# 파일 처리
# 읽기 처리 / 쓰기 처리

# (1) 스트림(stream, 물길) 연결
# w 쓰기 모드, a 추가해서 쓰기 모드, r 읽기 모드
파일 = open("경로", "모드")

# (2) 스트림을 통해 데이터 통신
문자열 = 파일.read()
print(문자열)

# (3) 스트림 해제
파일.close()

# with 구문 -> close 사용 안 해도 됨
with open("경로", "r") as 파일:
    문자열 = 파일.read()
    print(문자열)

# 파일 쓰기, w
with open("경로", "r") as 파일:
    파일.write("안녕하세요")

# 파일 추가해서 쓰기, a
with open("경로", "a") as 파일:
    파일.write("안녕하세요")

# 데이터 누적하는 프로그램
# 먼저 data.txt 파일을 만든다
파일  = open("data.txt", "r")
데이터 = 파일.read()
if 데이터 != "":
    print(파일.read().strip().split("\n"))
파일.close()

문자열 = input("> 데이터를 입력해주세요: ")
파일 = open("data.txt", "a")
파일.write(문자열.strip() + "\n")
파일.close()