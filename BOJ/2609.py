m,n = map(int, input().split())

max = 1

def findMax(a, b):
    first = None
    second = None
    if a > b:
        first = a
        second = b
    else:
        first = b
        second = a
    if first % second == 0:
        return None, second, True
    else:
        return second, int(first%second), False

a = m
b = n
isMax = False
while True:
    a, b, isMax = findMax(a, b)
    if isMax:
        max = b
        break

print(max)

def findMin(a, b, max):
    return a*b//max

print(findMin(m,n,max))