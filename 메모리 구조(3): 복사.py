# 메모리 구조(3): 복사 => 매우매우매우매우 중요!!!
# 변수를 변수에 할당하면[복사하면]
# 스택에 있는 것이 할당[복사]되는 것이다!
a = 10
b = a
a = 20
print(a) # 20
print(b) # 10

# 주소를 스택에 저장
a = [1, 2, 3, 4]
b = a
a = [1, 2, 3, 4, 5]
print(a) # [1, 2, 3, 4, 5]
print(b) # [1, 2, 3, 4]

# append 사용 => 중요
a = [1, 2, 3, 4]
b = a
a.append(5)
print(a) # [1, 2, 3, 4, 5]
print(b) # [1, 2, 3, 4, 5] -> 힙에 있는 리스트를 조작했기 때문에 a와 b에 있는 내용이 함께 변경된 것

# 최종확인
a = 10
b = [1, 2, 3, 4]
print(a, b)

def function_a(c, d):
    c = 20
    d = [5, 6, 7, 8]
function_a(a, b)
print(a, b)

def function_b(c, d):
    c = 30
    d.extend([9, 10])
function_b(a, b)
print(a, b)
