def solution(participant, completion):
    answer = ''
    check = {}
    for i in range(len(participant)):
        if participant[i] not in check:
            check[participant[i]] = 1
        else:
            check[participant[i]] += 1
    
    for i in range(len(completion)):
        check[completion[i]] -= 1

    for i, num in check.items():
        if num != 0:
            answer = i
            break

    return answer
