from sys import stdin

cur_left = list(stdin.readline())
cur_left.pop()
cur_right = []

n = int(stdin.readline())

for i in range(n):
    op = stdin.readline().split()
    if op[0] == 'L' and cur_left != []:
        cur_right.append(cur_left.pop())
    elif op[0] == 'D' and cur_right != []:
        cur_left.append(cur_right.pop())
    elif op[0] == 'B' and cur_left != []:
        cur_left.pop()
    elif op[0] == 'P':
        cur_left.append(op[1])

for i in range(len(cur_left)):
    print(cur_left[i], end='')

cur_right.reverse()
for i in range(len(cur_right)):
    print(cur_right[i], end='')
print()