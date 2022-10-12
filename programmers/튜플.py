def solution(s):
    s = s.replace('{','')

    arr = []
    tmp = []
    num = ''
    for i in range(len(s) - 1):
        if s[i] == '}' or s[i] == ',':
            if num != '':
                tmp.append(int(num))
                num = ''
            if s[i] == '}':
                arr.append(tmp)
                tmp = []
        else:
            if s[i].isdigit():
                num = num + s[i]

    arr.sort(key=len)

    result = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            result.append(arr[i][j])
        tmp = dict.fromkeys(result) # 리스트 값들을 key로 변경
        result = list(tmp) # 다시 dictionary를 리스트로 변경
    return result
