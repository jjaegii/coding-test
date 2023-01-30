n,m,v = map(int, input().split())

vertex = [[False] * (n+1) for _ in range(n+1)] # vertex = [[False] * (n+1)] * (n+1)는 리스트 안의 요소 리스트들이 모두 같은 참조값을 가짐
visited = [False] * (n+1)

for i in range(m):
    start, to = map(int, input().split())
    vertex[start][to] = vertex[to][start] = True

def DFS(v):
    visited[v] = True
    print(v, end=' ')

    for i in range(1, n+1):
        if vertex[v][i] and visited[i] == False:
            DFS(i)

DFS(v)
print()

visited = [False] * (n+1)
stack = []
def BFS(v):
    stack.append(v)
    visited[v] = True

    while len(stack) != 0:
        vert = stack.pop(0)
        print(vert, end=' ')
        for i in range(1, n+1):
            if vertex[vert][i] and visited[i] == False:
                stack.append(i)
                visited[i] = True

BFS(v)
    
