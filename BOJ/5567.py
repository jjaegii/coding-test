n = int(input()) # 동기 수
m = int(input()) # 리스트 길이

friends = [[False] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    friends[a][b] = friends[b][a] = True
    
def bfs():
    q = []
    q.append(1)
    visited[1] = 1
    while len(q) != 0:
        who = q.pop(0)
        
        for i in range(n+1):
            if friends[who][i] and not visited[i]:
                q.append(i)
                visited[i] = visited[who] + 1

bfs()

count = 0
for i in range(n+1):
    if visited[i] in [2,3]:
        count += 1

print(count)