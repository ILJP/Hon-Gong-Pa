# 함수는 변수에 저장할 수 있다
def call_10_times():
    pass

a = call_10_times()
print(a) # None 출력

a = call_10_times
print(a) # <function call_10_times at 어쩌구저쩌구>

a() # 이것도 가능, call_10_times()와 같은 것

# 함수를 매개변수로 전달하기
# 매개변수로 전달되는 함수 = 콜백함수
def call_10_times(콜백함수):
    for i in range(10):
        콜백함수(i) # 콜백함수에 매개변수 전달하기

def print_hello(매개변수):
    print("안녕하세요!", 매개변수)

call_10_times(print_hello) # 매개변수를 함수로 입력해서 전달

# 콜백함수 활용 예(1): map()
# 리스트 각각의 요소에 함수를 적용해서 새로운 이터레이터를 리턴
# 이터레이터 = map(함수, 리스트)
def power(숫자):
    return 숫자 ** 2
A = [1, 2, 3, 4, 5]
이터레이터 = map(power, A)
print(list(이터레이터))
print([ # 리스트 내포로 구현하기
    # 표현식
    숫자 ** 2
    # 반복문
    for 숫자 in range(1, 5 + 1)
])

# 콜백함수 활용 예(2): filter()
# filter(함수, 리스트)
# 리스트의 요소를 함수에 전달했을 때 
# 결과로 True가 나오는 녀석들을 모아서 새로운 이터레이터 만듦
def 홀수인가요(숫자):
    if 숫자 % 2 == 1:
        return True
    else:
        return False

A = [1, 2, 3, 4, 5]
이터레이터 = filter(홀수인가요, A)
print(list(이터레이터))
print([ # 리스트 내포로 표현하기
    # 표현식
    숫자
    # 반복문
    for 숫자 in range(1, 5 + 1)
    # 조건문
    if 숫자 % 2 == 1
])