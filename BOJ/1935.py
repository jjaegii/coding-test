n = int(input())
postfix = list(input())

alpha = {}
stack = []
for i in range(len(postfix)):
    if postfix[i].isalpha():
        if postfix[i] not in alpha:
            n = float(input())
            alpha[postfix[i]] = n
        else:
            n = alpha[postfix[i]]
        stack.append(n)
        continue
    b = stack.pop()
    a = stack.pop()
    if postfix[i] == '*':
        cal = a*b
    elif postfix[i] == '/':
        cal = a/b
    elif postfix[i] == '+':
        cal = a+b
    elif postfix[i] == '-':
        cal = a-b
    stack.append(cal)

print("{:.2f}".format(stack.pop()))
