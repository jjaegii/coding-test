k = int(input())

list = []
for i in range(k):
    n = int(input())
    if n == 0:
        list.pop() # 정수가 0일 경우에 지울 수 있는 수가 있음을 보장하므로 예외처리 x
        continue
    list.append(n)

print(sum(list))