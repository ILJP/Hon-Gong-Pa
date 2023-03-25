# 재귀 함수(2): 피보나치 수열
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        f(n - 1) + f(n - 2)
print(f(3))
print(f(4)) # but print(f(35))를 하면 매우 느림 => 메모화 필요!

# 메모화
memo = {} # 1: 1, 2: 1를 넣으면 if n==1, n==2도 필요없음
def f(n):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
       temp = f(n - 1) + f(n - 2) # temp = 임시
       memo[n] = temp
       return temp
