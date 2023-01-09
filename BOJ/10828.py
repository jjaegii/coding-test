from sys import stdin

n = int(stdin.readline())

list = []

for i in range(n):
    op = stdin.readline().split()
    if op[0] == "push":
        list.append(op[1])
    elif op[0] == "pop":
        if len(list) == 0:
            print(-1)
            continue
        print(list.pop())
    elif op[0] == "size":
        print(len(list))
    elif op[0] == "empty":
        if len(list) == 0:
            print(1)
            continue
        print(0)
    else:  # top
        if len(list) == 0:
            print(-1)
            continue
        print(list[len(list)-1])
