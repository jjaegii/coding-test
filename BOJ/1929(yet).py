input = input().split(' ')
m = int(input[0])
n = int(input[1])


def isPrime(num):  # 시간초과 뜸
    count = 0
    for i in range(num):
        if num % (i+1) == 0:
            count += 1
        if count > 2:
            return -1
    return 1


for i in range(m, n+1):
    if isPrime(i) == 1:
        print(i)
