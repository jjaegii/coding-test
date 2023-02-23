from sys import stdin

R, C = map(int, stdin.readline().split())

board = []

for _ in range(R):
    row = list(map(str, stdin.readline()))
    board.append(row)

move = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # left, down, right, up
alphabets = [0] * 26
maxcell = 0


def backtracking(row, col, cell):
    global maxcell
    maxcell = max(maxcell, cell)

    for i in range(4):
        new_row = row + move[i][0]
        new_col = col + move[i][1]
        if new_row < 0 or new_row >= R:
            continue
        if new_col < 0 or new_col >= C:
            continue
        if not alphabets[ord(board[new_row][new_col])-65]:
            alphabets[ord(board[new_row][new_col])-65] += 1
            backtracking(new_row, new_col, cell+1)
            alphabets[ord(board[new_row][new_col])-65] -= 1


alphabets[ord(board[0][0]) - 65] += 1
backtracking(0, 0, 1)
print(maxcell)
