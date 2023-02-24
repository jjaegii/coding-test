n, m = map(int, input().split())
zido = []
dist = [[0] * m for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    zido.append(row)
    if 2 in row:
        start = (i, row.index(2))

move = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # left, down, right, up


def bfs(start):
    q = []
    q.append((start[0], start[1]))
    while q:
        row, col = q.pop(0)

        for i in range(4):
            new_row = row + move[i][0]
            new_col = col + move[i][1]
            if new_row < 0 or new_row >= n:
                continue
            if new_col < 0 or new_col >= m:
                continue
            if dist[new_row][new_col] == 0 and zido[new_row][new_col] == 1:
                q.append((new_row, new_col))
                dist[new_row][new_col] = dist[row][col] + 1

    for i in range(n):
        for j in range(m):
            if dist[i][j] == 0 and zido[i][j] == 1:
                dist[i][j] = -1


bfs(start)
for i in range(n):
    for j in range(m):
        print(dist[i][j], end=' ')
    print()
