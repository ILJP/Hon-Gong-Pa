# max()함수와 min()함수
a = [52, 273, 32, 103, 57]

print(max(a)) # 273
print(min(a)) # 32

print(max(52, 273, 32, 103, 57)) # 273
print(min(52, 273, 32, 103, 57)) # 32

print(max(*a)) # 273, *은 전개연산자
print(min(*a)) # 32

# sum() 함수 - 숫자가 아닌 게 있다면 오류 발생
print(sum(a)) # 517

# reversed() 함수 - 결과: 한 번만 사용 가능!
for i in reversed(range(0, 10)):
    print(i) # 9 8 7 6 5 4 3 2 1 0(세로로 하나씩)

# enumerate() 함수 - 일회용
fruits = ["바나나", "사과", "포도"]
a = enumerate(fruits)
print(list(a)) # [(0, '바나나'), (1, '사과'), (2, '포도')]

for i, fruit in enumerate(fruits):
    print(i, fruit)

# items() 함수
a = {
    "이름": "바나나",
    "가격": 1500,
    "원산지": "말레이시아"
}
for 키, 값 in a.items():
    print(키, 값)
    
