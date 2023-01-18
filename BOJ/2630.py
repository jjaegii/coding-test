n = int(input())

paper = [[0] * n] * n

for i in range(n):
    paper[i] = list(input().split())

white = 0
blue = 0

def cut(x,y,n):
    global white, blue
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != color:
                cut(x, y, n//2)
                cut(x+n//2, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
    if color == '0': # white
        white += 1
    else:
        blue += 1

cut(0,0,n)
print(white)
print(blue)