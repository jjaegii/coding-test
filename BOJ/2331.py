A, P = map(int, input().split())

arr = set()
q = []

num = A
while True:
    q.append(num)
    arr.add(num)
    num = list(map(int, str(num)))
    sum = 0
    for i in range(len(num)):
        sum += num[i] ** P
    num = sum
    if num in arr:
        print(q.index(num))
        break
