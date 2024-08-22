move_types = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}

n = int(input())
plans = input().split()

x = 1
y = 1

for plan in plans:
    nx = x + move_types[plan][0]
    ny = y + move_types[plan][1]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)

