# 불 자료형 변환, bool()
None, 숫자 0(0.0), 빈 컨테이너(빈 문자열) 등 => False
이외의 다른 자료들 => True

# 불 자료형 자동 변환
i = input("입력해주세요: ")
i = i.strip()

if not i == "":
    print("입력한 내용:", i)
else:
    print("프로그램을 다시 실행해주세요")

# pass 키워드
i = input("입력해주세요: ")
i = i.strip()

if i:
    pass
else:
    print("프로그램을 다시 실행해주세요")

# raise NotImplementedError
i = input("입력해주세요: ")
i = i.strip()

if i:
    raise NotImplementedError
else:
    print("프로그램을 다시 실행해주세요")

# 간단한 대화 프로그램
i = input("입력: ")

if "안녕" in i:
    print("안녕하세요")
elif "몇 시" in i:
    from pytz import timezone
    from datetime import datetime
    today = datetime.now(timezone('Asia/Seoul'))
    print(f"> 지금은 {today.hour}시입니다.")
else:
    print(">", i)

# 나누어 떨어지는 숫자
i = int(input("정수를 입력해주세요"))

if i%2 == 0:
    print(f"{i}는 2로 나누어 떨어지는 숫자입니다")
else:
    print(f"{i}는 2로 나누어 떨어지는 숫자가 아닙니다")

if i%3 == 0:
    print(f"{i}는 3로 나누어 떨어지는 숫자입니다")
else:
    print(f"{i}는 3로 나누어 떨어지는 숫자가 아닙니다")

if i%4 == 0:
    print(f"{i}는 4로 나누어 떨어지는 숫자입니다")
else:
    print(f"{i}는 4로 나누어 떨어지는 숫자가 아닙니다")

if i%5 == 0:
    print(f"{i}는 5로 나누어 떨어지는 숫자입니다")
else:
    print(f"{i}는 5로 나누어 떨어지는 숫자가 아닙니다")
