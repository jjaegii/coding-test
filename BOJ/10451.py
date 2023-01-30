import sys
sys.setrecursionlimit(10**6)

n = None
array = []
visited = []

t = int(input())

def dfs(v):
    visited[v] = True
    next = array[v]

    if visited[next] == False:
        dfs(next)

for i in range(t):
    n = int(input())
    array = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)

    cycle = 0

    for i in range(1, n+1):
        if visited[i] == False:
            cycle += 1
            dfs(i)

    print(cycle)
