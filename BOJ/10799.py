list = list(input())
stack = 0
res = 0

for i in range(len(list)):
    if list[i] == '(':
        stack += 1
    elif list[i] == ')':
        stack -= 1
        if list[i-1] == '(':
            res += stack
        else:
            res += 1

print(res)
