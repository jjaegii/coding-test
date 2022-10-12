import math

n, k = input().split()
n = int(n)
k = int(k)
arr = []
for i in range(n):
    arr.append(int(input()))

total = 0
for i in range(len(arr)):
    total = total + arr[i];

start = 1
maxlen = total / k

count = 0
while True:
    mid = math.floor((maxlen + start) / 2)
    for i in range(n):
        count = count + math.floor(arr[i]/mid)
    if start > maxlen:
        print(mid)
        break
    if count >= k:
        start = mid + 1
    else:
        maxlen = mid - 1
    count = 0
