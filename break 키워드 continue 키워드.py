# break 키워드: 반복문 전체를 벗어날 때 사용하는 구문
i = 0

while True:
    print(f"{i}번째 반복입니다.")
    i += 1

    a = input("> 종료하시겠습니까?(y/n): ")
    if a in ["y", "Y"]:
        print("반복문을 종료합니다.")
        break

# continue 키워드: 현재 반복을 넘어갈 때 사용하는 구문
numbers = [5, 15, 6, 20, 7 ,25]

for number in numbers:
    if number < 10:
        continue
    print(number)
