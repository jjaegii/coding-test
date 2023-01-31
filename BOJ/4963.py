import sys
sys.setrecursionlimit(10**6)

w = None
h = None
zido = []
visited = []

# left, down, right, up, left_down, left_up, right_down, right_up
move = [[0, -1], [1, 0], [0, 1], [-1, 0], [1, -1], [-1, -1], [1, 1], [-1, 1]]


def dfs(row, col):
    visited[row][col] = True

    for i in range(8):
        if row+move[i][0] < 0 or row+move[i][0] >= h:
            continue
        if col+move[i][1] < 0 or col+move[i][1] >= w:
            continue
        if zido[row+move[i][0]][col+move[i][1]] and not visited[row+move[i][0]][col+move[i][1]]:
            dfs(row+move[i][0], col+move[i][1])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    zido = []
    visited = [[False] * (w) for _ in range(h)]
    for i in range(h):
        row = list(map(int, input().split()))
        zido.append(row)

    count = 0
    for i in range(h):
        for j in range(w):
            if zido[i][j] and not visited[i][j]:
                count += 1
                dfs(i, j)
    print(count)
