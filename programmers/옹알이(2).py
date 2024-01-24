def check_alpha(word):
    for i in word:
        if i.isalpha():
            return False
    return True

def check_con_num(word):
    for i in word:
        if i.isalpha():
            word = word.replace(alphas[i], '')
            
    print(word)

    if len(word) != 0:
        w_list = list(word)
        w = w_list[0]
        for i in range(1, len(w_list)):
            if w == w_list[i]:
                return False
            w = w_list[i]
            
    return True
    
def solution(babbling):
    answer = 0
    
    can = ["aya", "ye", "woo", "ma"]
    
    tmp = []
    for word in babbling:
        for c in can:
            if c == "aya":            
                word = word.replace(c ,'1')
            if c == "ye":            
                word = word.replace(c ,'2')
            if c == "woo":            
                word = word.replace(c ,'3')
            if c == "ma":            
                word = word.replace(c ,'4')
        tmp.append(word)
    
    print(tmp)
    
    for a in tmp:
        if check_alpha(a) and check_con_num(a):
            answer += 1
    
    return answer