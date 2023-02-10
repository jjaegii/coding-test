import math
import heapq
from sys import stdin

n = int(stdin.readline()) # 도시
m = int(stdin.readline()) # 노선

routes = [[] for _ in range(n+1)]
costs = [math.inf] * (n+1)

for _ in range(m):
    start, to, cost = list(map(int, stdin.readline().split()))
    routes[start].append((to, cost))

def bfs(start):
    q = []
    costs[start] = 0
    heapq.heappush(q, (start, costs[start]))
    while len(q) != 0:
        start, start_cost = heapq.heappop(q)

        if costs[start] < start_cost:
            continue

        for to, to_cost in routes[start]:
            new_cost = start_cost + to_cost
            if costs[to] > new_cost:
                costs[to] = new_cost
                heapq.heappush(q, (to, costs[to]))

start, end = list(map(int, stdin.readline().split()))
bfs(start)

print(costs[end])
    