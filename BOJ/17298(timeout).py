n = int(input())

a = list(map(int, input().split()))
res = []

for i in range(n):
    for j in range(i+1, n):
        if a[i] < a[j]:
            res.append(a[j])
            break
    else:
        res.append(-1)

for i in range(n):
    print(res[i], end=' ')