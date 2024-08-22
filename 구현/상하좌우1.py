dx = [0, 0, -1, 1] 
dy = [-1, 1, 0, 0]

n = int(input())
plans = input().split()

x = 1
y = 1

for plan in plans:
    nx = 0
    ny = 0
    if (plan == "L"):
        nx = x + dx[0] # nx라는 변수를 만들고, 하단에서 범위를 벗어나지 않는지 확인 후에 x에 값을 대입한다
        ny = y + dy[0]
    elif (plan == "R"):
        nx = x + dx[1]
        ny = y + dy[1]
    elif (plan == "U"):
        nx = x + dx[2]
        ny = y + dy[2]
    else:
        nx = x + dx[3]
        ny = y + dy[3]
    if (nx < 1 or ny < 1 or nx > n or ny > n):
        continue
    x, y = nx, ny

print(x, y)

