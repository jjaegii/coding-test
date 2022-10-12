// BOJ 15649
// N과 M(1)
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX 8

int num[MAX] = { };
bool check[MAX] = { false, };
int M, N;

void backtracking(int count) {
	if (count == N) {
		for (int i = 0; i < count; i++) {
			printf("%d ", num[i]);
		}
		printf("\n");
		return;
	}

	for (int i = 0; i < M; i++) {
		if (check[i] == false) {
			check[i] = true;
			num[count] = i + 1;
			backtracking(count + 1);
			check[i] = false;
		}
	}

}

int main() {
	scanf("%d %d", &M, &N);

	backtracking(0);
}
