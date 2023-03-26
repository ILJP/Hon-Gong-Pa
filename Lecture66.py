# 이터러블: 반복할 수 있는 것(반복문 뒤에 넣을 수 있는 것)
# Interate + able
# 리스트, 튜플, 딕셔너리

# 이터레이터: 반복하는 녀석(이터러블을 만드는 방법 중 하나)
# Interate + or
# 이터레이터 만드는 법
## - 제너레이터 표현식 (리스트 내포와 매우 유사, [] 대신()을 쓰면 됨)
제너레이터표현식 = (
    i * i
    for i in 범위
)
print(제너레이터표현식) # <generator object <genexpr> at 어쩌구저쩌구> *참고: gen expr -> generator expression
print(next(제너레이터표현식)) # next: 내부 요소를 하나씩 꺼냄

## - 제너레이터 함수
def 제너레이터함수(): # yield 키워드가 있으면 제너레이터 함수로 간주
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

제너레이터 = 제너레이터함수()
print(next(제너레이터))
print(next(제너레이터))
print(next(제너레이터))
print(next(제너레이터))
print(next(제너레이터))

## - 이터레이터 클래스
=> 얘는 좀 어려움