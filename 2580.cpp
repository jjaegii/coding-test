#include <stdio.h>
#include <stdlib.h>

int board[9][9];
int empty = 0;
int e_row[81];
int e_col[81];

void sudoku(int);

int main() {
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			scanf("%d", &board[i][j]);
			if (board[i][j] == 0) {
				e_row[empty] = i;
				e_col[empty++] = j;
			}
		}
	}
	sudoku(0);
}

void sudoku(int count) {
	if (empty == count) {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				printf("%d ", board[i][j]);
			}
			printf("\n");
		}
		exit(0);
	}

	int row = e_row[count];
	int col = e_col[count];
	bool num[10] = { false, };

	for (int i = 0; i < 9; i++) {
		num[board[row][i]] = true;
		num[board[i][col]] = true;
	}

	int rowcell = (row / 3) * 3;
	int colcell = (col / 3) * 3;
	for (int r = rowcell; r < rowcell + 3; r++) {
		for (int c = colcell; c < colcell + 3; c++) {
			if (board[r][c] != 0) num[board[r][c]] = true;
		}
	}

	for (int k = 1; k < 10; k++) {
		if (!num[k]) {
			board[row][col] = k;
			sudoku(count + 1);
			board[row][col] = 0;
		}
	}
}
