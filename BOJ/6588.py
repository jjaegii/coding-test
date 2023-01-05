from sys import stdin

def isPrime(num):
    if num == 1:
        return False
    if num in [2,3,5,7]:
        return True
    for i in range(2, int((num**0.5)+1)):
        if num % i == 0:
            return False

    return True

def goldbach(n):
    half = int(n/2)
    i = 3
    # 홀수 소수만 나타내면 됨
    while i <= half:
        if isPrime(i) and isPrime(n-i):
            print(str(n) + " = " + str(i) + " + " + str(n-i))
            return
        i += 2
    print("Goldbach's conjecture is wrong.")

while True:
    n = int(stdin.readline())
    if n == 0:
        break
    goldbach(n)