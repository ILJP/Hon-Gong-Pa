# 불 자료형
True
False

# 비교 연산자
 = 할당 연산자
 == 비교 연산자

# 논리 연산자
단항: not
이항: and(둘 다 True일 때 결과 True ), or(둘 중 하나만 True여도 결과 True)

# 날짜/시간 구하는 방법
import datetime
import pytz

seoul = pytz.timezone("Asia/Seoul")
now = datetime.datetime.now(seoul)

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
now.year,
now.month,
now.hour,
now.day,
now.minute,
now.second,
))