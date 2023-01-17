n = int(input())

def hanoi(n, A, B, C): # start, end, mid
    if n <= 0:
        return

    hanoi(n-1, A, C, B)
    print(A, B)
    hanoi(n-1, C, B, A)

print(2**n - 1)
hanoi(n, 1, 3, 2)