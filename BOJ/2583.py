m, n, k = map(int, input().split())
a = [[False] * n for _ in range(m)]

for _ in range(k):
    left_x, left_y, right_x, right_y = map(int, input().split())
    for i in range(left_y, right_y):
        for j in range(left_x, right_x):
            a[i][j] = True

move = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # right, down, right, up


def bfs(row, col):
    q = []
    q.append((row, col))
    a[row][col] = True
    count = 1
    while q:
        row, col = q.pop(0)

        for i in range(4):
            new_row = row + move[i][0]
            new_col = col + move[i][1]
            if new_row < 0 or new_row >= m:
                continue
            if new_col < 0 or new_col >= n:
                continue
            if not a[new_row][new_col]:
                a[new_row][new_col] = True
                q.append((new_row, new_col))
                count += 1

    return count


counts = []
for i in range(m):
    for j in range(n):
        if not a[i][j]:
            counts.append(bfs(i, j))

counts.sort()
print(len(counts))
for i in range(len(counts)):
    print(counts[i], end=' ')
