# 집 N개가 수직선 위에 존재 
# 집의 좌표는 x1, ..., xN / 같은 좌표 X
# 공유기 C개 설치. 한 집에서는 공유기 하나만 설치 가능하고 인접한 두 공유기 사이의 거리를 가능한 크게


N, C = map(int, input().split())
x = [int(input()) for _ in range(N)]
x.sort()

start = 1 # 최소 거리
end = x[-1] - x[0] # 최대 거리
max_dis = 0 # 거리 넣을 변수 설정

while start <= end :
    mid = (start + end) // 2 # 두 공유기 사이의 거리가 mid라면 몇 개의 집에 설치 가능한가?
    pre_x = x[0] # 현재의 집
    count = 1
    
    for i in range(1, N) :
        if x[i] >= pre_x + mid :
            pre_x = x[i] 
            count += 1 
    # 설치 가능한 집 개수가 C보다 크면 공유기 사이의 거리를 늘린다.
    if count >= C :
        start = mid + 1
        max_dis = mid
    # 설치 가능한 집의 개수가 C보다 작으면 공유기 사이 거리를 줄인다.
    else :
        end = mid - 1

print(max_dis)
