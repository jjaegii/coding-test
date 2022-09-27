#include <iostream>
#include <queue>
using namespace std;

#define MAX 1001

int N, M, V; // vertex 개수, edge 개수, start vertex
bool vertex[MAX][MAX] = { false, };
bool visited[MAX] = { false, };
queue<int> q;

void DFS(int from) {
	cout << from << " ";
	visited[from] = true;
	for (int i = 1; i <= N; i++) {
		if (vertex[from][i] && !visited[i]) {
			visited[i] = true;
			DFS(i);
		}
	}
}

void BFS(int from) {
	visited[from] = true;
	q.push(from);
	while (!q.empty()) {
		int num = q.front();
		cout << num << " ";
		q.pop();
		for (int i = 1; i <= N; i++) {
			if (vertex[num][i] && !visited[i]) {
				q.push(i);
				visited[i] = true;
			}
		}
	}
}

int main() {
	cin >> N >> M >> V;
	for (int i = 0; i < M; i++) {
		int from, to;
		cin >> from >> to;
		vertex[from][to] = vertex[to][from] = true; // 양방향
	}

	DFS(V);
	cout << endl;
	for (int i = 1; i <= N; i++)
		visited[i] = false; // init
	BFS(V);
}
