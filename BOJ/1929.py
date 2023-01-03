'''
에라토스테네스의 체(https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4)를 썼으나
간과한 사실이 위 경우는 120까지의 숫자만 존재하므로 11보다 작은 수의 배수들 (2,3,5,7)만으로도 가능하다는 점에서 2,3,5,7만 이용했다.
그러므로 2,3,5,7만이 아닌 해당 수의 제곱근보다 작은 수들로 나눗셈이 된다면 소수가 아니라는 점을 이용했다.
'''

m,n = map(int, input().split())

array = [True for i in range(n+1)]
array[1] = False

for i in range(m, n+1):
    if i in [2,3,5,7]:
        continue
    for j in range(2, int(i**(1/2)+1)):
        if i%j == 0:
            array[i] = False
            break

for i in range(m, n+1):
    if array[i]:
        print(i)