# 조기 리턴
memo = {1: 1, 2: 1}
def f(n):
    if n in memo:
        return memo[n]
    
    temp = f(n - 1) + f(n - 2) # temp = 임시
    memo[n] = temp
    return temp

# 리스트 평탄화
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output.extend(flatten(item))
        else:    
            output.append(item)
    return output