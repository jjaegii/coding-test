L, C = map(int, input().split())
alphas = list(map(str, input().split()))
alphas.sort()

vowels = ['a', 'e', 'i', 'o', 'u']
length = 0
passwords = []


def backtracking(password, count):
    if count == L:
        vowel = 0
        for i in range(len(vowels)):
            vowel += password.count(vowels[i])

        if vowel < 1:  # 최소 한 개의 모음
            return
        if len(password) - vowel < 2:  # 최소 두 개의 자음
            return
        passwords.append("".join(password))

    for i in range(C):
        if alphas[i] not in password:
            no_flag = False
            for j in range(len(password)):
                if password[j] > alphas[i]:
                    no_flag = True
                    break
            if not no_flag:
                password.append(alphas[i])
                backtracking(password, count+1)
                password.pop()


password = []
backtracking(password, 0)

for i in range(len(passwords)):
    print(passwords[i])
