# map() 직접 구현하기
def my_map(콜백함수, 리스트):
    output = []
    for 요소 in 리스트:
        output.append(콜백함수(요소))
    return



# filter() 직접 구현하기
def my_filter(콜백함수, 리스트):
    output = []
    for 요소 in 리스트:
        if 콜백함수(요소): # == True 생략
            ouput.append(요소)
        return output
