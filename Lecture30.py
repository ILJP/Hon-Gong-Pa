# 중첩 리스트
a = [[1, 2, 3], [4, 5, 6, 7], [8,9 ]] # 2차원 리스트

# 전개 연산자
*리스트 => 리스트 전개 연산자

## (1) 리스트 내부
a = [1, 2, 3]
b = [*a, *a] => [1, 2, 3, 1, 2, 3]

## (2) 함수의 매개변수 위치
date = [2022, 8 ,10, 14, 14]

"{}년 {}월 {}일 {}시 {}분".format(date[0], date[1], date[2], date[3], date[4])
는 아래와 같음
"{}년 {}월 {}일 {}시 {}분".format(*date)