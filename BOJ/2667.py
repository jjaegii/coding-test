n = int(input())
zido = []
visited = [[False] * (n) for _ in range(n)]

for i in range(n):
    row = list(map(int, input()))
    zido.append(row)

move = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # left, down, right, up

count = 0
numbers = []  # 단지당 집 수 저장
parts = 0  # 단지 수


def dfs(row, col):
    global count
    visited[row][col] = True
    count += 1

    for i in range(4):
        if row+move[i][0] < 0 or row+move[i][0] >= n:
            continue
        if col+move[i][1] < 0 or col+move[i][1] >= n:
            continue
        if zido[row+move[i][0]][col+move[i][1]] and not visited[row+move[i][0]][col+move[i][1]]:
            dfs(row+move[i][0], col+move[i][1])


for i in range(n):
    for j in range(n):
        if zido[i][j] and not visited[i][j]:
            parts += 1
            dfs(i, j)
            numbers.append(count)
            count = 0

print(parts)
numbers.sort()
for i in range(parts):
    print(numbers[i])
