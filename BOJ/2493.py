n = int(input())

tower = list(map(int, input().split()))
stack = []  # (값, 인덱스) 쌍
response = []

for i in range(n):
    while len(stack) != 0:
        if stack[-1][0] > tower[i]:
            response.append(stack[-1][1] + 1)
            break
        else:
            stack.pop()
    if len(stack) == 0:
        response.append(0)
    stack.append((tower[i], i))

for i in range(len(response)):
    print(response[i], end=' ')
