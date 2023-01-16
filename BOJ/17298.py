n = int(input())

a = list(map(int, input().split()))
stack = []
res = []

while len(a) != 0:
    while len(stack) and stack[len(stack)-1] <= a[len(a)-1]:
        stack.pop()
    if len(stack) == 0:
        res.append(-1)
    else:
        res.append(stack[len(stack)-1])
    stack.append(a[len(a)-1])
    a.pop()

for i in range(n):
    print(res.pop(), end=' ')
