'''
# brute force 방식으로 구했을 때는 효율성 테스트에서 0점을 맞게 된다.
def solution(prices):
    answer = []
    for i in range(0, len(prices)-1):
        if prices[i] < min(prices[i+1:]):
            answer.append(len(prices[i+1:]))
        else:
            cnt = 0
            for j in prices[i+1:] :
                if prices[i] <= j :
                    cnt += 1
                else :
                    cnt+= 1
                    break
            answer.append(cnt)
    answer.append(0)
    return answer
'''

# 위의 경우에는 O(N^2)인데, 스택으로 풀면 최악의 경우 O(N^2)로 동일하지만, 최선의 경우 O(2N)으로 끝낼 수 있다.
# 아래와 같은 방식으로 풀면 스택 방식으로 풀 수 있다.

def solution(prices):
    # answer = 몇초 후 가격이 떨어지는지 저장하는 배열 시작값을 len(prices)-1부터 시작해서 0까지로
    answer = [len(prices)-i-1 for i in range(len(prices))]
    
    # stack = prices의 인덱스를 차례로 담아두는 배열
    stack = [0]
    
    for i in range(1, len(prices)):
        while stack:
            index = stack[-1]
            # 주식 가격이 떨어졌다면 
            if prices[index] > prices[i]:
                answer[index] = i - index
                stack.pop()
            # 떨어지지 않았다면 다음 시점으로 넘어감 (주식 가격이 계속 증가하고 있다)
            else:
                break
                
        # 스택에 추가
        # 다음 시점으로 넘어갔을 때 다시 비교 대상이 될 예정이다.
        stack.append(i)
    return answer
