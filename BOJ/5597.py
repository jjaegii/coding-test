students = [False] * 31
for _ in range(28):
    students[int(input())] = True

for i in range(1, 31):
    if not students[i]:
        print(i)
