# https://programmers.co.kr/learn/courses/30/lessons/42842


def solution(brown, yellow):
    answer = []
    total = brown + yellow 
    
    for y in range(1, total + 1):
        # 약수인지 확인
        if (total / y) % 1 == 0:
            x = total / y
            # 값이 brown이 4면의 개수와 같은지 확인
            if x >= y:                      
                if 2 * x + 2 * y - 4 == brown: 
                    return [x, y]
