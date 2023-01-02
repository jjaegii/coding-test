n = int(input())
inputs = input().split(' ')


def isPrime(n):
    count = 0
    for i in range(n):
        if n % (i+1) == 0:
            count += 1
        if count > 2 or n == 1:
            return -1
    return 1


count = 0
for i in range(n):
    if isPrime(int(inputs[i])) == 1:
        count += 1

print(count)
