n = int(input())

list = []
def sort():
    for i in range(len(list)):
        minidx = i
        for j in range(i, len(list)):
            if list[minidx] > list[j]:
                minidx = j
        
        tmp = list[i]
        list[i] = list[minidx]
        list[minidx] = tmp

for i in range(n):
    list.append(int(input()))

sort()
for i in range(n):
    print(list[i])