F,S,G,U,D = map(int, input().split())

visited = [0] * (F+1)

def bfs():
    q = []
    q.append(S)
    visited[S] = 1
    while len(q) != 0:
        c = q.pop(0)
        if c == G:
            return visited[c]
        
        for i in (c+U,c-D):
            if 1 <= i <= F and not visited[i]:
                q.append(i)
                visited[i] = visited[c] + 1
        
    return None

buttons = bfs()
if buttons == None:
    print("use the stairs")
else:
    print(buttons-1)