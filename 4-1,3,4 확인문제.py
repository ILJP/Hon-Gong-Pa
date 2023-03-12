# 4-2 확인문제
character = {}
for i in range(0, 4):
    character[key_list[i]] = value_list[i]
print(character)

# 4-3 확인문제
limit = 10000
i = 1
sum_value = 0
while sum_value <= limit:
    sum_value += i
    i += 1
print(f"{i-1}를 더할 때 {limit}을 넘으며 그때의 값은 {sum_vale}입니다")

# 4-4 확인문제
## 최대값 구하기
a = [27, 53, 103, 273, 32]

현재최대값 = a[0]
for i in a:
    if 현재최대값 < i:
        현재최대값 = i
print(현재최대값)
#-----------------------------------
현재최대값 = 0
a = 0
b = 0

for i in range(1, 99+1):
    j = 100 - i
    if 현재최대값 < i * j:
        a = i
        b = j
        현재최대값 = i * j

print("최대가 되는 경우: {} * {} = {}".format(a, b, 현대최대값))
