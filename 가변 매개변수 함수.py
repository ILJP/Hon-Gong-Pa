# 가변 매개변수 함수
def print_n_times(횟수, *문자열):
    for i in range(횟수):
        for 요소 in 문자열:
            print(요소)

# 전개 연산자와 조합하기
문자열목록 = ["안녕", "하세요"]
print_n_times(2, *문자열목록) # 리스트의 요소가 하나씩 풀림

# 주의 사항
가변 매개변수 뒤에는 일반 매개변수가 올 수 없음!
