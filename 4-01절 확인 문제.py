# 4-01절 확인 문제

## 확인문제 4번
=> 주기적으로 반복되는 수열을 만들 때는 나머지 연산자를 사용한다!

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in number:
    ouput[(number - 1) % 3].append(number)

print(output)
