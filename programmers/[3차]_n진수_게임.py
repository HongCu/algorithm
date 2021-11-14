# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 

# n 진법에 맞게 구하는 함수 정의
# 거기서 t*m번 계산하고 마지막 형태를 내뱉을 수 있도록 만들기
# 그 중에서 튜브가 대답해야하는 경우 p-1, p-1+m, p-1+2m의 형태일 것
# 이 과정을 t회 반복하도록 구현

def solution(n, t, m, p):
    
    all_answer = ''
    
    def mod_change(num, notation):
        temp = "0123456789ABCDEF"
        # divmod : 몫과 나머지를 구해준다.
        q, r = divmod(num, notation)

        if q == 0:
            return temp[r]
        else:
            # q가 0이 될 때까지 더 계산할 수 있도록 재귀적으로 불러옴
            return mod_change(q, notation) + temp[r]
    
    for i in range(t*m):
        all_answer += str(mod_change(i, n))
    
    # for문 형식으로 range정의로 구현하는 방법
    '''
    tube_answer = ''
    for j in range(p-1, t*m, m):
        tube_answer += all_answer[j]
    '''
    # 리스트 컴프리헨션 형태로 구현하는 방법
    tube_answer = [all_answer[j] for j in range(p-1, t*m, m)]
    tube_answer = ''.join(tube_answer)
    
    # while문 형태로 구현하는 방법
    '''
    tube_answer = ''
    while len(tube_answer) < t:
        tube_answer += all_answer[p-1]
        p += m
    '''    
    return tube_answer
