# 기본 매개변수
def test(a = 10):
    print(a)

test() # a = 10
test(20) # a = 20
test(a = 30) # a = 30

# 기본 매개변수의 위치
매개변수 중에서 가장 마지막에 위치

# 기본 매개변수와 가변 매개변수
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times("문자열", "안녕하세요", n=2)

# print()함수의 sep, end 매개변수
print("안", "녕", "하", "세", "요", sep = "::", end = "\n")

# 딕셔너리 매개변수
def 함수(*가변, **딕셔너리):
    print(가변, 딕셔너리)

함수("안", "녕", "하", 
   a=10, b=20, c=30)