import sys
sys.setrecursionlimit(10**6)

# DFS 한번 돌려보고 visited가 안돼있으면 다시 DFS 또 돌리는 식으로 진행
n, m = map(int, sys.stdin.readline().split())
vertex = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    vertex[u][v] = vertex[v][u] = True

count = 0 # 연결요소 개수

def DFS(v):
    visited[v] = True

    for i in range(1, n+1):
        if vertex[v][i] and visited[i] == False:
            DFS(i)

def check(): # 모든 정점에 다녀왔는지 체크
    for i in range(1, n+1):
        if visited[i] == False:
            return i # 다녀오지 않은 정점이 있다면 리턴

    return False

while True:
    vert = check()
    if vert == False:
        break
    count += 1
    DFS(vert)

print(count)
    

