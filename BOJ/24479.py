# 2차원 배열로 구성할 경우 메모리 초과가 발생했음
# 메모리 절약을 위해 연결된 노드만 추가하는 식으로 진행함

import sys

sys.setrecursionlimit(10**9)

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


def dfs(v):
    global count
    visited[v] = True
    result[v] = count

    for i in vertex[v]:
        if not visited[i]:
            count += 1
            dfs(i)


dfs(R)

print(*result[1:], sep="\n")
