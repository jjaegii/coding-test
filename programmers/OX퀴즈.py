def solution(quiz):
    answer = []
    
    for i in quiz:
        q, a = i.split("=")
        q = eval(q)
        a = eval(a)
        
        if q == a:
            answer.append("O")
        else:
            answer.append("X")
    
    return answer