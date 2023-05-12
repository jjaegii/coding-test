import sys

N, M, R = map(int, sys.stdin.readline().split())

result = [0] * (N + 1)
visited = [False] * (N + 1)
vertex = [[] for _ in range(N + 1)]

for i in range(M):
    start, to = map(int, sys.stdin.readline().split())
    vertex[start].append(to)
    vertex[to].append(start)

for i in range(1, N + 1):
    vertex[i].sort()

count = 1


def bfs(start):
    global count
    q = []
    q.append(start)
    visited[start] = True
    result[start] = count
    count += 1

    while q:
        v = q.pop(0)

        for i in vertex[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                result[i] = count
                count += 1


bfs(R)

print(*result[1:], sep="\n")
