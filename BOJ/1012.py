import sys
from sys import stdin

sys.setrecursionlimit(10**6)

t = int(stdin.readline())
farm = []
visited = []
move = [[0,-1],[1,0],[0,1],[-1,0]] # left, down, right, up

def dfs(row,col):
    visited[row][col] = True
    
    for i in range(len(move)):
        if row + move[i][0] < 0 or row + move[i][0] >= n:
            continue
        if col + move[i][1] < 0 or col + move[i][1] >= m:
            continue
        if farm[row+move[i][0]][col+move[i][1]] and not visited[row+move[i][0]][col+move[i][1]]:
            dfs(row+move[i][0],col+move[i][1])
        

for i in range(t):
    count = 0
    m, n, k = map(int, stdin.readline().split())
    farm = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for i in range(k):
        col, row = map(int, stdin.readline().split())
        farm[row][col] = 1

    for i in range(n):
        for j in range(m):
            if farm[i][j] and not visited[i][j]:
                count += 1
                dfs(i,j)

    print(count)