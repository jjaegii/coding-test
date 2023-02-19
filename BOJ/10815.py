from sys import stdin

n = int(stdin.readline())
n_list = list(map(int, stdin.readline().split()))
n_list.sort()
m = int(stdin.readline())
m_list = list(map(int, stdin.readline().split()))

for i in range(m):
    start = 0
    end = n-1
    exist = 0
    while end >= start:
        mid = int((start+end)/2)
        if m_list[i] > n_list[mid]:
            start = mid + 1
            continue
        if m_list[i] < n_list[mid]:
            end = mid - 1
            continue
        if m_list[i] == n_list[mid]:
            exist = 1
            break

    print(exist, end=' ')
