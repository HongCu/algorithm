def calcul(N, K, coin_list):
    # 큰 동전부터 차례대로 나오면서 K를 변경해주자 
    cnt = 0
    for coin in coin_list:
        # K원 중에서 coin*cnt원 만큼을 나누고 cnt를 갱신하고 K도 나머지로 갱신
        cnt += K // coin
        K = K % coin
        # 남은 돈이 없으면 for문 빠져나가기
        if K == 0:
            break
    return cnt

def main():
    # N 동전 종류 개수, K 총 가진 금액
    N, K = map(int, input().split())
    coin_list = [int(input()) for _ in range(N)]
    # 오름차순으로 주어진거 계산하기 편하게 내림차순 정렬
    coin_list.sort(reverse=True)
    print(calcul(N, K, coin_list))

if __name__ == '__main__':
    main()

'''
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
'''