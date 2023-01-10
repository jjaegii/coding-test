list = [True] * 123457 * 2

for i in range(2, len(list)):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            list[i] = False
            break

def countPrime(num):
    count = 0
    for i in range(num+1, num*2+1):
        if list[i] == True:
            count += 1

    print(count)

while True:
    n = int(input())
    if n == 0:
        break
    countPrime(n)