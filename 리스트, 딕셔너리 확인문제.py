# 확인문제 3번
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number not in counter:
        counter[number] = 0
    counter[number] += 1
print(counter)

# 확인문제 4번
character = {
    "name": "기사",
    "level": 12,
    "items": {
    "sword": "불꽃의 검",
    "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
    }

for key in character:
    if type(character[key]) is dict:
        for 키 in character[key]:
            print(f"{키}: {character[key][키]}")
    elif type(character[key]) is list:
        for 요소 in character[key]:
            print(f"skill: {요소}")
    else:
        print(f"{key} : {character[key]}")
