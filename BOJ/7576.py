from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())

tomatoes = []
for _ in range(n):
    row = list(map(int, stdin.readline().split()))
    tomatoes.append(row)

q = deque()
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            q.append((i, j))

move = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # left, down, right, up
while q:
    x, y = q.popleft()

    for i in range(4):
        x_move = x+move[i][0]
        y_move = y+move[i][1]
        if x_move < 0 or x_move >= n:
            continue
        if y_move < 0 or y_move >= m:
            continue
        if tomatoes[x_move][y_move] == 0:
            tomatoes[x_move][y_move] = tomatoes[x][y] + 1
            q.append((x_move, y_move))

res = -1
for i in range(n):
    if 0 in tomatoes[i]:
        res = -1
        break
    res = max(res, max(tomatoes[i]) - 1)

print(res)
