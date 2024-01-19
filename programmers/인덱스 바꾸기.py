def solution(my_string, num1, num2):
    answer = ''
    
    str = list(my_string)
    word1 = str[num1]
    word2 = str[num2]
    
    str[num1] = word2
    str[num2] = word1
    
    for i in str:
        answer += i
    
    return answer