T = int(input())


def count(num):
    if num == 0:
        print("1 0")
        return
    if num == 1:
        print("0 1")
        return
    list = [0, 1]
    for i in range(num-1):
        list.append(list[0]+list[1])
        list.pop(0)
    print(list[0], list[1])


for i in range(T):
    count(int(input()))
