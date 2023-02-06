import sys
sys.setrecursionlimit(10**6)

n = int(input())

zone = []
visited = [[False] * n for _ in range(n)]
for _ in range(n):
    row = list(map(int, input().split()))
    zone.append(row)

max_safe_zone = 0
move = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # left,down,right,up


def dfs(row, col, rain_deep):
    visited[row][col] = True

    for i in range(4):
        if row + move[i][0] < 0 or row + move[i][0] >= n:
            continue
        if col + move[i][1] < 0 or col + move[i][1] >= n:
            continue
        if zone[row+move[i][0]][col+move[i][1]] > rain_deep and not visited[row+move[i][0]][col+move[i][1]]:
            dfs(row+move[i][0], col+move[i][1], rain_deep)


for rain_deep in range(0, 101):
    safe_zone = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if zone[i][j] > rain_deep and not visited[i][j]:
                dfs(i, j, rain_deep)
                safe_zone += 1
    max_safe_zone = max(max_safe_zone, safe_zone)

print(max_safe_zone)
