def solution(s):
    num_add=[]
    num_substract=[]
    
    # 문자열 s에서 숫자 골라내기
    for i in s:
        if i.isdigit():
            num_add.append(int(i))
    
    print(num_add) # 확인용

# 문자열 s에서 빼야 할 숫자 골라내기 (Z 발견하면 Z 바로 앞의 숫자 append)
    for k in enumerate(s.split()):  # 공백 제하고 리스트에 담아서 루프 & 생각 좀 .. 더 ..
        if k == 'Z':
            num_substract.append()   # append함수에 인자로 'Z'의 '리스트 인덱스-1' 값을 넣고 싶음
        
        result_add = sum(num_add)
        result_sub = sum(num_substract)
    
        result = result_add - result_sub

    print(result)

s='1 2 Z 5 Z 6 1 3'

# sol_01

s_split = s.split() # 공백 제하고 리스트에 담기
answer = 0

def sol_01(s):
    for i in s_split:
        if i != 'Z':
            answer += int(i)  # answer=0 만들러 지금에서야 올라가도 ㄱㅊ아

print(answer)
