'''
4 6
101111
101010
101011
111011
'''
from collections import deque

def bfs(matrix, x, y, dx, dy, N, M):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # 총 네 곳의 방향으로 이동한다.
            nx, ny = x + dx[i], y + dy[i]
            # 만약 이 이동한 방향이 범위안에 들어온다면
            if 0 <= nx < N and 0 <= ny < M: 
                # 그리고 방문하지 않은 지점이라면
                if matrix[nx][ny] == 1:
                    # 이전의 기록된 수를 업데이트한다.
                    matrix[nx][ny] += matrix[x][y]
                    # 그리고 다시 이 nx와 ny를 넣어 queue를 돌린다.
                    queue.append((nx, ny))

    return matrix[N-1][M-1]


def main():
    N, M = map(int, input().split())
    matrix = [list(map(int, input())) for i in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    print(bfs(matrix, 0, 0, dx, dy, N, M))

if __name__ == "__main__":
	main()