from sys import stdin
import heapq

move = [[0,-1],[1,0],[0,1],[-1,0]] # left, down, right, up
def dfs():
    money[0][0] = cave[0][0]
    q = []
    heapq.heappush(q, (0,0,money[0][0]))
    while len(q) != 0:
        row, col, cost = heapq.heappop(q)

        for i in range(4):
            if row + move[i][0] < 0 or row + move[i][0] >= n:
                continue
            if col + move[i][1] < 0 or col + move[i][1] >= n:
                continue
            new_cost = cost + cave[row+move[i][0]][col+move[i][1]]
            if money[row+move[i][0]][col+move[i][1]] > new_cost:
                q.append((row+move[i][0],col+move[i][1], new_cost))
                money[row+move[i][0]][col+move[i][1]] = new_cost

problem = 1
while True:
    n = int(stdin.readline())
    if n == 0:
        break

    cave = []
    money = [[2000] * n for _ in range(n)]

    for _ in range(n):
        row = list(map(int, stdin.readline().split()))
        cave.append(row)
    
    dfs()
    
    print(f"Problem {problem}: {money[n-1][n-1]}")

    problem += 1
