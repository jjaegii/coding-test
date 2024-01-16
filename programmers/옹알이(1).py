def check_alpha(word):
    for i in word:
        if i.isalpha():
            return False
    return True
    
def solution(babbling):
    answer = 0
    
    can = ["aya", "ye", "woo", "ma"]
    
    tmp = []
    for word in babbling:
        for c in can:
            word = word.replace(c ,' ')
        tmp.append(word)
    
    print(tmp)
    
    for a in tmp:
        if check_alpha(a):
            answer += 1
    
    return answer