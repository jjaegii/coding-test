def solution(my_string):
    answer = 0
    alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
    for i in alphas:
        if i in my_string:
            my_string = my_string.replace(i, ' ')
    
    for i in my_string.split():
        answer += int(i)
    
    return answer