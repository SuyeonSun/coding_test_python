# (1, 1) -> (N, M)
# 0: 괴물 o
# 최소 칸의 개수

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최단거리는 bfs
def bfs(i, j, cnt):
    queue = deque([[i, j, cnt]])
    while queue:
        x, y, cnt = queue.popleft()
        if (x == n-1 and y == m-1): # 놓쳤던 부분: 끝에 도달했을 때 return
            return cnt
        graph[x][y] = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if (nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
            if (graph[nx][ny] == 0):
                continue
            queue.append([nx, ny, cnt+1])
    return -1 # 핵심

print(bfs(0, 0, 1))
