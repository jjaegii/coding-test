n, m = map(int, input().split())

array = []
visited = [False] * (n+1)

# 재귀를 써야할거같음(백트래킹)
def sequence(n, m, target):
    if m == target:
        for i in range(len(array)):
            print(array[i], end=' ')
        print()

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            array.append(i)
            sequence(n, m, target+1)
            visited[i] = False
            array.pop()

sequence(n,m,0)
    