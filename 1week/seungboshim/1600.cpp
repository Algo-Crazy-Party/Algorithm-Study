#include <iostream>
#include <vector>
#include <stack>
#include <tuple>
#include <queue>

using namespace std;

int K, W, H;

int dx[12] = {1, 2, 2, 1, -1, -2, -2, -1, 1, 0, -1, 0};
int dy[12] = {-2, -1, 1, 2, 2, 1, -1, -2, 0, 1, 0, -1};

vector<vector<int>> map;
pair<bool, pair<int,int>> visited[200][200]; // 방문 여부, 경로 길이, 말 점프 횟수
stack<pair<int,int>> s;
queue<pair<int,int>> q;

void dfs(int x, int y) {
    s.push({x, y}); // 시작점
    visited[x][y] = {true, {0, 0}}; // 시작점 방문

    while (!s.empty()) {
        int currX = s.top().first; // 현재 X
        int currY = s.top().second; // 현재 Y
        s.pop();

        int currDist = visited[currX][currY].second.first; // 현재까지의 거리
        int jumpCnt = visited[currX][currY].second.second; // 현재까지의 말 점프 횟수
        cout << "말점프: " << jumpCnt << "번 함\n";
        
        if (currX == H - 1 && currY == W - 1) { // 도착
            cout << currDist << '\n';
            return;
        }

        for (int i = 0; i < 12; i++) {
            // 말 점프 다 씀
            if (jumpCnt == K) { 
                i = 8; // 일반 이동만 가능
            }

            // 말 점프
            if (i < 8 && jumpCnt < K) { 
                jumpCnt++;
            }

            // 이동하기
            int nextX = currX + dx[i]; 
            int nextY = currY + dy[i];
            cout << "다음 위치: " << nextX << ", " << nextY << '\n';

            // 범위 내, 길막 X 
            if (nextX >= 0 && nextX < H && nextY >= 0 && nextY < W && map[nextX][nextY] != 1) { 
                visited[nextX][nextY] = {true, {currDist + 1, jumpCnt}}; // 방문 ㄱㄱ
                s.push({nextX, nextY});
            } else continue;
        }
    }
}

void bfs(int x, int y) {
    q.push({x, y});
    visited[x][y] = {true, {0, 0}};
    
}

int main() {
    cin >> K >> W >> H;
    map.resize(H, vector<int>(W, 0));

    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cin >> map[i][j];
        }
    }

    // dfs(0, 0);

    return 0;
}