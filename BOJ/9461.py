T = int(input())


def P(num):
    if num >= 1 and num <= 3:
        print(1)
        return
    list = [1, 1, 1]
    for i in range(num-3):
        list.append(list[0]+list[1])
        list.pop(0)
    print(list[-1])


for i in range(T):
    P(int(input()))
