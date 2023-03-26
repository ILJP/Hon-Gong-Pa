# 재귀 함수(1): 기본

# 팩토리얼 연산
# - 반복문으로 구현
def factorial(n):
    ouput = 1
    for i in range(1, n + 1):
        ouput *= i
    return ouput
print(factorial(2))
print(factorial(3))
print(factorial(4))

# -재귀함수로 구현
## 수학의 수열의 점화식: 이웃한 항의 관계를 통해 수열을 나타내는 것
## 함수는 호출될 때 스택을 만들고, 리턴될 때 스택을 제거함
def factorial(n):
    if n == 1:
        return 1
    elif n >= 2:
        return n * factorial(n - 1)
