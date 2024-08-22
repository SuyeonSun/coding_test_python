# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, i, j):
    graph[i][j] = 1
    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        if (nx < 0 or ny < 0 or nx >= n or ny >= m):
            continue
        if (graph[nx][ny] == 0):
            dfs(graph, nx, ny)  

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(graph, i, j)
            cnt += 1

print(cnt)