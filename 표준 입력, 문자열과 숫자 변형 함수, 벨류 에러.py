# 표준 입력
input(prompt) 함수
*prompt: 입력을 요청하는 문자열

*주의할 점
a = input("숫자1: ") => 10 입력
b = input("숫자2: ") => 20 입력
print(a+b) = 1020 (30이 나오지 않음, 문자열이기 때문에)

# 문자열 -> 숫자
int(), float()

# 숫자 -> 문자열
str()

# ValueError
int("hello")와 같이 해당 자료형으로 변환할 수 없는 문자를 입력했을 때 발생
