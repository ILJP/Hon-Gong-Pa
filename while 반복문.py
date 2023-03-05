# while 반복문
while 조건:
    복합구문 # 조건이 참이라면 반복

# while 반복문을 for 반복문처럼 사용하기
i = 0
while i < 10:
    print(f"{i}번째 반복입니다.")
    i += 1

# while 반복문: 상태 기반 반복
a = [1, 2, 1, 2]
value = 2
while value in a:
    a.remove(value)

# while 반복문: 시간 기반 반복
## 유닉스 시간: 1970년 1월 1일 0시 0분 0초을 기준으로 하는 시간
import time
start = time.time() # 한 번 입력하므로써 고정
now = time.time()   # 한 번 입력하므로써 고정

while now < start + 5:
    print(now, start + 5)
    now = time.time() # 현재시간을 불러와 계속 바꿔줌
