# 함수와 리턴
def f(x):
    #값을 들고 돌아가라
    return x + 1
    # x + 1을 들고 돌아가라!
    # return 뒤에 아무것도 없으면 None

# 함수 사용해보기
def 함수(매개변수):
    변수 = 초기화
    # 여러가지 처리
    # 여러가지 처리
    # 여러가지 처리
    return 변수

def sum_all(start, end):
    # 항등원으로 초기화
    output = 0
    for i in range(start, end + 1):
        output += i
    return output

print(sum_all(1, 100))
