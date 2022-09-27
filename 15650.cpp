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
		if (check[i] == false) {
			check[i] = true;
			num[count] = i;
			backtracking(i + 1, count + 1); // backtracking(start + 1, count + 1)과 헷갈렸다 제대로 알자.
			check[i] = false;
		}
	}
}

int main() {
	scanf("%d %d", &M, &N);

	backtracking(1, 0);
}
