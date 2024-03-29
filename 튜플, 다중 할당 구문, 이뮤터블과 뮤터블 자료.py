# 튜플
a = (1, 2, 3)
print(a[0])
print(a[1])
print(a[2])

## 요소를 하나 갖는 튜플
b = (1, )

## 튜플 괄호 생략
a = 1, 2 ,3 # (1, 2, 3)
b = 1, # (1, )

## 튜플과 리스트의 차이(요소 변경 불가능)
리스트는 값의 변경이 가능하지만, 튜플은 불가능

# 다중 할당 구문
[a, b] = [10, 20]
(a, b) = (10, 20) # a, b = 10, 20
a, b = [10, 20]

# 튜플과 함수 리턴
def a():
    return 10, 20, 30
b, c, d = a()
print(b, c, d) # 10, 20, 30

# 요소를 변경할 수 없다!
## 자료: 뮤터블 자료 + 이뮤터블 자료

# 이뮤터블 자료 -> 딕셔너리의 키로 사용 가능
## 변수에 넣었을 떼
## 스택에 있는 값을 변경해야만 값을 변경할 수 있는 자료
a = 10
a = 20 # 숫자들은 이뮤터블
b = True
b = False # 불도 이뮤터블
c = "안녕하세요"
c = "안녕히가세요" # 문자열도 이뮤터블
c[1] = "가" # 오류 발생
튜플도 이뮤터블

# 뮤터블 자료
## 변수에 넣었을 때
## 스택에 있는 값을 변경하지 않아도 값을 변경할 수 있는 자료
리스트, 딕셔너리는 뮤터블
