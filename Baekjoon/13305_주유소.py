# 그리디 문제

# N-1 번째 거리까지 도달하도록 for문을 통해 한 거리당의 처리하는 함수
def search(N, oil_cost, distance) :
    
    # 최초 비용은 고정되어 있으므로 일단 이를 구함
    min_cost = distance[0] * oil_cost[0]
    
    # 다음 주유소까지 가야 할 현재 비용과 거리 거리
    city_cost = oil_cost[0]
    city_to_city = 0
    
    for i in range(1, N-1):
        # 오일가격이 이전보다 저렴한지 확인
        if oil_cost[i] < city_cost:
            # 저렴하다면 그 곳에서 다음곳 도착까지 주유
            min_cost += city_cost * city_to_city
            # 이동할 거리를 다시 갱신
            city_to_city = distance[i]
            # 비용 갱신
            city_cost = oil_cost[i]
        # 저렴하지 않다면 거리만 추가해줌    
        else:
            # 이동할 거리만 갱신
            city_to_city += distance[i]
        # 최종 코스트를 계산
        if i == N - 2 : 
            min_cost += city_cost * city_to_city
    return min_cost


def main():
    # 도시 개수
    N = int(input())
    # 도로의 길이
    distance = list(map(int, input().split()))
    # 주유소의 리터당 가격
    oil_cost = list(map(int, input().split()))
    print(search(N, oil_cost, distance))

if __name__ == '__main__' :
    main()