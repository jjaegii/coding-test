n = int(input())
list = []
for i in range(n):
    list.append(int(input()))

stack = []
num = 0
res = []

for i in range(len(list)):
    while num < list[i]:
        num += 1
        stack.append(num)
        res.append('+')
    if stack.pop() == list[i]:
        res.append('-')
    else:
        print('NO')
        exit(0)

for i in range(len(res)):
    print(res[i])