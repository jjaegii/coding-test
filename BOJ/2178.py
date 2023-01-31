n, m = map(int, input().split())

maze = [[0] * (m) for _ in range(n)]
visited = [[0] * (m) for _ in range(n)]

for i in range(n):
    row = list(map(int, input()))
    maze[i] = row

move = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # left, down, right, up


def bfs():
    q = []
    q.append((0, 0))
    visited[0][0] = 1
    while len(q) != 0:
        row, col = q.pop(0)

        for i in range(4):
            if row + move[i][0] < 0 or row + move[i][0] >= n:
                continue
            if col + move[i][1] < 0 or col + move[i][1] >= m:
                continue
            if maze[row+move[i][0]][col+move[i][1]] and not visited[row+move[i][0]][col+move[i][1]]:
                q.append((row+move[i][0], col+move[i][1]))
                visited[row+move[i][0]][col+move[i][1]] = visited[row][col] + 1


bfs()
print(visited[n-1][m-1])
