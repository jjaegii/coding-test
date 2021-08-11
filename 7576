#include <iostream>
#include <queue>
using namespace std;

int board[1001][1001];
int day[1001][1001] = { 0, };
int dx[4] = { 1,0,-1,0 }; // 가로
int dy[4] = { 0,1,0,-1 }; // 세로

int main() {
	int n, m; // n = 세로, m = 가로
	cin >> m >> n; // 가로 세로
	
	int count = 0;
	queue<pair<int, int>> Q;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> board[i][j];
			if (board[i][j] == 1) { // 익은 토마토의 경우를 미리 큐에 넣어둔다
				// 예제 입력 3의 경우 때문에 큐에 미리 넣지않으면 첫번째 익은 토마토에서
				// bfs를 실행할 시 마지막 익은 토마토를 건드려버리기 때문
				Q.push(make_pair(i, j));
				continue;
			}
			if (board[i][j] == 0) // 안익은 토마토 개수 세기
				count++;
			day[i][j] = -1; // 접근하지 않았다는 표시
		}
	}

	int result = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (board[i][j] == -1 || board[i][j] == 0)
				continue;
			while (!Q.empty()) {
				pair<int, int> tmp = Q.front();
				Q.pop();
				for (int dir = 0; dir < 4; dir++) {
					int ny = tmp.first + dy[dir];
					int nx = tmp.second + dx[dir];
					if (ny < 0 || nx < 0 || ny >= n || nx >= m)
						continue;
					if (board[ny][nx] == -1 || day[ny][nx] != -1)
						continue;
					count--; // 안익은 토마토에 접근할때
					day[ny][nx] = day[tmp.first][tmp.second] + 1;
					board[ny][nx] = 1;
					Q.push(make_pair(ny, nx));
					if (day[ny][nx] > result)
						result = day[ny][nx];
				}
			}
		}
	}
	
	if (count != 0) // 안익은 토마토가 남아있는 경우
		result = -1;
	cout << result << endl;
}
