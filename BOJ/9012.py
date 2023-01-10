n = int(input())

def isVps(vps, stack):
    for j in range(len(vps)):
        if vps[j] == '(':
            stack.append(True)
        else:
            if len(stack) == 0:
                print('NO')
                return
            stack.pop()
    if len(stack) != 0:
        print('NO')
    else:
        print('YES')
    

for i in range(n):
    vps = list(input())
    isVps(vps, stack=[])            