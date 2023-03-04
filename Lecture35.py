# 범위: 특정한 범위 내부의 정수들을 나열하는 자료형
## range(a)
0부터 a까지의 정수를 범위로 나열, a는 포함하지 않음
=> 특정 횟수만큼 반복하는 경우
ex)
for i in range(10):
    pass # print("반복입니다")

## range(a, b)
a부터 b까지의 정수를 범위로 나열, b는 포함하지 않음
=> 2개 넣는 경우: 반복 변수를 사용하는 경우
ex)
for i in range(0, 10):
    pass # print(f"{i}번째입니다!"")

## range(a, b, c)
a부터 b까지의 정수를 범위로 나열, b는 포함하지 않음, c만큼 건너뛰면서 범위를 생성
=> 반대로 반복하는 경우
ex)
for i in range(10, -1, -1):
    print(f"{i}번째입니다!")
