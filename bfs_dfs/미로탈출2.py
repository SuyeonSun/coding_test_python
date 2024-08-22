from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque([[i, j]])
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if (nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
            if (graph[nx][ny] == 0):
                continue
            if (graph[nx][ny] == 1): # 값을 바로 graph에 누적하는 경우, 1일 경우에만 실행하도록 조건 필수
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

bfs(0, 0)
print(graph[n-1][m-1])
