import sys
h, w = map(int, sys.stdin.readline().split())

zido = []
visited = [[0] * (w) for _ in range(h)]

for _ in range(h):
    row = list(map(str, sys.stdin.readline()))
    zido.append(row)

move = [[0,-1],[1,0],[0,1],[-1,0]] # left, down, right, up
def bfs(start_row, start_col):
    q = []
    q.append((start_row,start_col))
    visited[start_row][start_col] = 1
    moves = set()
    while len(q) != 0:
        row, col = q.pop(0)

        for i in range(4):
            if row + move[i][0] < 0 or row + move[i][0] >= h:
                continue
            if col + move[i][1] < 0 or col + move[i][1] >= w:
                continue
            if zido[row+move[i][0]][col+move[i][1]] == 'L' and not visited[row+move[i][0]][col+move[i][1]]:
                q.append((row+move[i][0],col+move[i][1]))
                visited[row+move[i][0]][col+move[i][1]] = visited[row][col] + 1
                moves.add(visited[row][col]+1)

    if len(moves) == 0:
        return 0
    return max(moves) - 1

shortest = 0
for i in range(h):
    for j in range(w):
        if zido[i][j] == 'L':
            count = bfs(i,j)
            if count > shortest:
                shortest = count
            visited = [[0] * (w) for _ in range(h)]

print(shortest)