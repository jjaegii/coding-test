from sys import stdin

n = int(stdin.readline())
files = {}
for _ in range(n):
    file = stdin.readline().split('.')[1]
    if file not in files:
        files[file] = 1
    else:
        files[file] += 1

files = dict(sorted(files.items()))
for key, value in files.items():
    print(key.rstrip(), value)
