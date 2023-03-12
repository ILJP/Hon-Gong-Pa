# 확인문제 2번
## 진법 변환
f"{10:b}" # 이진수 변환
f"{10:o}" # 팔진수 변환
f"{10:x}" # 십육진수 변환
int("1010", 2) # 이진수를 십진수로 변환
int("12", 8) # 팔진수를 십진수로 변환
int("a", 16) # 십육진수를 십진수로 변환
a = []
for i in range(1, 100+1):
    변환 = f"{i:b}"
    if 변환.count("0") == 1:
        print(i, ":", 변환)
        a.append(i)
print("합계:", sum(a))