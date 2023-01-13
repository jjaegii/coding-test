n = int(input())

tower = list(map(int, input().split()))
response = []

for i in range(n):
    for j in range(i+1, n):
        if tower[-(j+1):-j] >= tower[-(i+1):-i]:
            response.append(n-j)
            break
    else:
        response.append(0)

for i in range(n):
    print(response.pop(), end=' ')