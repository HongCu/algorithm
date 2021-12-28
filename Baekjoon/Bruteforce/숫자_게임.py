from itertools import combinations

N = int(input())

nums = [(input().split()) for _ in range(N)]
maxs = []
for idx in nums:

    max_value = 0
    for combs in list(combinations(idx, 3)) :
        values = map(int, combs)
        plus = 0
        for i in values:
            plus += i
        plus = int(str(plus)[-1:])

        if plus > max_value :
            max_value = plus
    maxs.append(max_value)


for i in range(N-1, -1, -1): 
  if maxs[i] == max(maxs):  
    print(i + 1)
    break
