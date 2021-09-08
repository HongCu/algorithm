from itertools import permutations

# 데이터 받기
N = int(input())
k = int(input())
num_list = [input() for _ in range(N)]

# 순열을 통해서 개수 확인
nPk = list(permutations(num_list, k))
com_list = []
for first in nPk:
    combination = ''
    for second in range(k):
        combination += first[second]
    com_list.append(combination)
# 순열 겹치는 것 set으로 제거 후 최종 개수 구하기
print(len(set(com_list)))
