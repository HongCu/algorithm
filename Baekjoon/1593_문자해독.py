# 온라인 저지 회원 수 N
N = int(input())
# 회원 입력
member = []
for i in range(N):
    A = list(map(str, input().split()))
    A[0] = int(A[0])
    member.append(A)

# member.sort()를 하면 x[1]의 순서도 같이 이동
member.sort(key = lambda x : x[0])

for i in range(len(member)):
    print(member[i][0], member[i][1])
