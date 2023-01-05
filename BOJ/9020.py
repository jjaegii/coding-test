# 해당 수의 절반부터 시작해서 소수가 있는데까지 찾아보면 될듯
# ex) 1000의 경우 500부터 시작해서 a = 499->498->497순으로 해서 소수가 발견되면 1000 - a도 소수인지 확인

t = int(input())

def isPrime(num):
    if num in [2,3,5,7]:
        return True
    for i in range(2, int((num**0.5)+1)):
        if num % i == 0:
            return False

    return True

def goldbach(n):
    half = int(n/2)
    for i in range(half):
        if isPrime(half-i) and isPrime(half+i):
            print(str(half-i) + " " + str(half+i))
            break

for i in range(t):
    n = int(input())
    goldbach(n)