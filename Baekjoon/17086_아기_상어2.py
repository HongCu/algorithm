'''
5 4
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1
'''

from collections import deque
# BFS 형식으로 구현
def bfs(queue, dx, dy, N, M, matrix) :
  while queue:
    x, y = queue.popleft()
    
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < M:
        if matrix[nx][ny] == 0:
          matrix[nx][ny] = matrix[x][y] + 1
          queue.append((nx, ny))
  return queue, matrix
            
def max_count(N, M, matrix) :
  max_value = 0
  for i in range(N):
    for j in range(M):
      if matrix[i][j] >= max_value:
        max_value = matrix[i][j] 
  return max_value - 1       


def main():
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 대각선 포함해서 움직일 수 있다고 했으니 각 인덱스 별로 갈 수 있는 길 8방향 생성
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    queue = deque()
    for column in range(M):
        for row in range(N):
            if matrix[row][column] == 1:
        # 1의 위치 넣기
                queue.append((row, column))

    bfs(queue, dx, dy, N, M, matrix)
    # 결국 문제에서 원하는 것은 갈 수 있는 안전거리의 최댓값이므로 이를 구해야 한다.
    print(max_count(N, M, matrix))



if __name__ == "__main__":
	main()
