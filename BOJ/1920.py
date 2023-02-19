from sys import stdin

n = int(stdin.readline())
n_row = list(map(int, stdin.readline().split()))
n_row.sort()
m = int(stdin.readline())
m_row = list(map(int, stdin.readline().split()))


for i in range(m):
    start = 0
    end = n-1
    exist = 0
    while end >= start:
        mid = int((start+end)/2)
        if m_row[i] < n_row[mid]:
            end = mid - 1
            continue
        if m_row[i] > n_row[mid]:
            start = mid + 1
            continue
        if m_row[i] == n_row[mid]:
            exist = 1
            break
    print(exist)
