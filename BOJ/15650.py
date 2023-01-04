n, m = map(int, input().split())

visited = [False] * (n+1)
array = []

def isBigger(num):
    if len(array) == 0:
        return True
    if num > max(array):
        return True
    else:
        return False

def backtracking(n, m, target):
    if target == m:
        for i in range(len(array)):
            print(array[i], end = ' ')
        print()
    
    for i in range(1, n+1):
        if not visited[i] and isBigger(i):
            visited[i] = True
            array.append(i)
            backtracking(n, m, target+1)
            visited[i] = False
            array.pop()

backtracking(n, m, 0)