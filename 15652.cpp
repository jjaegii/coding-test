#include <stdio.h>

#define MAX 9

int num[MAX] = { 0, };
bool check[MAX] = { false, };
int M, N;

void backtracking(int start, int count) {
	if (count == N) {
		for (int i = 0; i < count; i++) {
			printf("%d ", num[i]);
		}
		printf("\n");
		return;
	}

	for (int i = start; i <= M; i++) {
		num[count] = i;
		backtracking(i, count + 1);
	}
}

int main() {
	scanf("%d %d", &M, &N);

	backtracking(1, 0);
}
