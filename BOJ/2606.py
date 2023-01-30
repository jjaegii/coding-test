n = int(input())
m = int(input())

vertex = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    u,v = map(int, input().split())
    vertex[u][v] = vertex[v][u] = True

count = 0
def dfs(v):
    global count
    visited[v] = True

    for i in range(1, n+1):
        if vertex[v][i] and not visited[i]:
            count += 1
            dfs(i)

dfs(1)
print(count)