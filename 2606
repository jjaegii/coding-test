#include <iostream>
#include <queue>
using namespace std;

#define MAX 101

int N, M; // vertex 수, edge 수
bool vertex[MAX][MAX] = { false, };
bool visited[MAX] = { false, };
queue<int> q;
int infected = 0;

void BFS(int from) {
	visited[from] = true;
	q.push(from);
	while (!q.empty()) {
		from = q.front();
		q.pop();
		for (int i = 1; i <= N; i++) {
			if (vertex[from][i] && !visited[i]) {
				visited[i] = true;
				q.push(i);
				infected++;
			}
		}
	}
}

int main() {
	cin >> N >> M;
	for (int i = 0; i < M; i++) {
		int from, to;
		cin >> from >> to;
		vertex[from][to] = vertex[to][from] = true;
	}

	BFS(1);
	cout << infected;
}
