MAX = 100000
n, k = map(int, input().split())

visited = [0] * (MAX+1)

def bfs():
    q = []
    q.append(n)
    while len(q) != 0:
        c = q.pop(0)
        if c == k:
            print(visited[c])
            break
        
        for i in (c-1, c+1, c*2):
            if 0 <= i <= MAX and not visited[i]:
                q.append(i)
                visited[i] = visited[c]+1

bfs()