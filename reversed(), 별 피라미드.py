# reversed()
## 매개변수: 반복 가능한 것
## 결과: 그것을 뒤집은 것
## 결과 자료형: 이터레이터
##  -> list()를 사용해 리스트로 변환해서 결과 보기
ex)
for i in reversed(range(0, 10)):
    print(i)

# 별 피라미드
height = 10
for i in range(1, height+ 1):
    print("*" * i)

# N개의 별을 가로 방향으로 출력하는 반복문
N = 10
result = ""
for i in range(N):
    result += "*"
print(result)

# 최종 결과
height = 10
for i in range(1, height+ 1):
    result = ""
    for j in range(i):
        result += "*"
    print(result)

# 별 피라미드
height = 3
for i in range(1, height + 1):
    result = ""
    for j in range(height - i):
        result += " "
    for j in range(2 * i - 1):
        result += "*"
    print(result)
