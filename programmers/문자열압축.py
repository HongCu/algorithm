def solution(s):
    answer = len(s)
    # 자르는 구간 : cut_num  1 ~ half of len(s)
    for cut_num in range(1, len(s)//2 + 1): # 자를 단위
        result = ''
        cnt = 1
        tmp = s[:cut_num] # 단위문자열 초기화
        
        # cut_num이 돌면서 한 문장의 구간 돌면서 비교
        for i in range(cut_num, len(s)+cut_num, cut_num):
            if tmp == s[i:i+cut_num]:
                cnt += 1
            else:
                if cnt == 1:
                    result += tmp
                else:
                    result += str(cnt) + tmp
                tmp = s[i:i+cut_num]
                cnt = 1
        # answer 작은 값으로 변경    
        answer = min(answer, len(result))
    return answer
