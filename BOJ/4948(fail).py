'''
시간초과 발생 때문에
이전에 소수로 판정났던 수는 리스트에 추가 시켜놓고
리스트에 있다면 따로 계산하지 않는 절차를 부여했으나 실패
'''
        
def countPrime(n, ary):
    count = 0
    for i in range(n+1, 2*n+1):
        flag = True
        if i in ary:
            count += 1
            continue
        if i == 1:
            flag = False
            continue
        for j in range(2, int(i**(1/2)+1)):
            if i%j == 0:
                flag = False
                break
        if flag:
            count += 1
            ary.append(i)
    print(count)
    return ary
        
ary = []

while True:
    n = int(input())
    if n == 0:
        break
    ary = countPrime(n, ary)
