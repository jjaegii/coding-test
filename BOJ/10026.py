import sys
sys.setrecursionlimit(10**6)

n = int(input())

picture = []
visited = [[False] * n for _ in range(n)]

for _ in range(n):
    row = list(map(str, input()))
    picture.append(row)

move = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # left, down, right, up


def dfs(row, col):
    visited[row][col] = True
    color = picture[row][col]

    for i in range(4):
        if row+move[i][0] < 0 or row+move[i][0] >= n:
            continue
        if col+move[i][1] < 0 or col+move[i][1] >= n:
            continue
        if picture[row+move[i][0]][col+move[i][1]] == color and not visited[row+move[i][0]][col+move[i][1]]:
            dfs(row+move[i][0], col+move[i][1])


count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count += 1
            dfs(i, j)

print(count)


def blinddfs(row, col):
    visited[row][col] = True
    color = picture[row][col]

    for i in range(4):
        if row+move[i][0] < 0 or row+move[i][0] >= n:
            continue
        if col+move[i][1] < 0 or col+move[i][1] >= n:
            continue
        if color in ['R', 'G']:
            if picture[row+move[i][0]][col+move[i][1]] in ['R', 'G'] and not visited[row+move[i][0]][col+move[i][1]]:
                blinddfs(row+move[i][0], col+move[i][1])
        else:
            if picture[row+move[i][0]][col+move[i][1]] == color and not visited[row+move[i][0]][col+move[i][1]]:
                blinddfs(row+move[i][0], col+move[i][1])


count = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count += 1
            blinddfs(i, j)
print(count)
