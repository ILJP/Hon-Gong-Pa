# 람다: 간단한 함수를 간단하게 해주는 문법
def power(숫자):
    return 숫자 ** 2

power = lambda 숫자: 숫자 ** 2 # 위와 같음
print(power(10))

# 람다를 인라인 함수로 사용하기
A = [1, 2, 3, 4, 5]
이터레이터 = map(power = lambda 숫자: 숫자 ** 2, A)

# key 키워드 매개변수
A = [{
    "제목": "혼자 공부하는 파이썬",
    "가격": 18000
    }, {
    "제목": "혼자 공부하는 머신러닝 + 딥러닝",
    "가격": 26000
    }, {
    "제목": "혼자 공부하는 자바스크립트",
    "가격": 24000
    }]

def 가격(요소):
    return 요소["가격"]

print(min(A, key = 가격))
print(max(A, key = 가격))

print(min(A, key = lambda 책: 책["가격"]))
print(max(A, key = lambda 책: 책["가격"]))

A.sort(key = lambda 책: 책["가격"]) # 가격순으로 정렬
print(A)
