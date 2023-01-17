n = int(input())

def hanoi(n, start, end, mid): # A,B,C
    if n <= 0:
        return

    hanoi(n-1, start, mid, end) # A,C,B
    print(start, end)
    hanoi(n-1, mid, end, start) # C,B,A

print(2**n-1)
if n <= 20:
    hanoi(n, 1, 3, 2)
