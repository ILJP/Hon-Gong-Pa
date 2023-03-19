# 4장 도전 문제 4번
A = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
B = []

for a in A:
    if type(a) == list:
        for i in a:
            B.append(i)
    else:
        B.append(a)

# 위 아니면 아래 모두 가능 
for a in A:
    if type(a) == list:
        for i in a:
            # B.append(i)
            B += [i] # 리스트 결합 연산자는 리스트만 쓸 수 있다
    else:
        #B.append(a)
        B += [a]
print(B)
