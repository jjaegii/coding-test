def roll(A):
    tmp = A.pop()
    A.insert(0, tmp)

def solution(A, B):
    answer = 0
    
    A = list(A)
    B = list(B)
    
    for i in range(len(A)):
        if A == B:
            return answer
        roll(A)
        answer += 1
    
    return -1