from collections import deque
# 알아둘 사항 deque는 슬라이싱이 안된다....
# itertools의 islice(iterable, start, stop)을 사용할 수 있다.
from itertools import islice 


def solution(priorities, location):
    answer = 0
    # 안의 tuple로 두 가지 정보를 동시에 고려함
    prior_queue = deque([(v,i) for i,v in enumerate(priorities)])

    while prior_queue:
        # 더 큰 값이 있는지 확인
        item = prior_queue.popleft()
        # prior_queue가 없으면 런타임 에러가 난다.
        # 이유는 max가 고를 prior_queue가 존재하지 않을 수 있으므로.
        if prior_queue and max(prior_queue)[0] > item[0]:
            prior_queue.append(item)
        else:
            # 하나씩 빠져나가고 추가 안되면 answer 갱신
            answer += 1
            if item[1] == location:
                break
    return answer
