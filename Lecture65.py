# 간단한 CSV(Comma Separated Values, 콤마로 구분되어 있는 값들) 파일 읽고 쓰기

# BMI 데이터 만들기
# 랜덤하게 1명의 키와 몸무게
import random
한글 = lsit("가나다라마바사아자차카타파하")

파일 = open("human,txt", "w") # 파일 열기
파일.write("이름,몸무게,키\n")
for i in range(1000):
    이름 = random.choice(한글) + random.choice(한글)
    몸무게 = random.randrange(40, 120)
    키 = random.randrange(140, 200)
    파일.write(f"{이름}, {몸무게}, {키}\n")
# print("{},{},{}".format(이름, 몸무게, 키))
# print(",".join([이름, str(몸무게), str(키)]))
파일.close() # 파일 닫기


# BMI 분석하기(CSV 데이터 한 줄씩 읽기)
파일 = open("human.txt", "r")

for 한줄 in 파일:
    이름,몸무게,키 = 한줄.strip().split(",")

    if not 몸무게.isdigit():
        continue
    몸무게 = int(몸무게)
    키 = int(키)
    bmi = 몸무게 / (키 / 100) ** 2
    결과 = ""
    if 25 <= bmi:
        결과 = "과체중"
    if 18.5 <= bmi:
        결과 = "정상체중"
    else:
        결과 = "저체중"

    print("\n".join([
        f"이름: {이름}",
        f"몸무게: {몸무게}",
        f"키: {키}",
        f"BMI: {bmi}",
        f"결과: {결과}", ""
    ]))
파일.close()