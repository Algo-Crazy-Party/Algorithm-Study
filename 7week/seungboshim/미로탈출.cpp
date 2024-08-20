#include <string>
#include <vector>
#include <queue>

using namespace std;

int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};
int lx,ly;

int BFS(int sx, int sy, vector<string> maps, vector<vector<int>> &count, int row, int col, bool toLever) {
    queue<pair<int, int>> q;
    q.push({sx, sy});
    int x, y;

    while (!q.empty()) {
        x = q.front().first;
        y = q.front().second;
        
        q.pop();

        if ((toLever && maps[x][y] == 'L') || (!toLever && maps[x][y] == 'E')) {
            if (toLever) {
                lx = x;
                ly = y;
            }
            break; // 끝점 도착
        }

        for(int i=0; i<4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= row || ny < 0 || ny >= col || maps[nx][ny] == 'X') {
                continue;
            }
            
            if (count[nx][ny] == -1 || count[nx][ny] > count[x][y]+1) { // 미방문 or 방문했는데 더 짧은 거리있음
                count[nx][ny] = count[nx][ny] + 1;
                q.push({nx, ny});
            }
        }
    }
    
    return count[x][y];
}

int solution(vector<string> maps) {
    int answer = -1;
    // 레버 칸으로 먼저 ㄱㄱ?
    // dfs bfs
    int row = maps.size(); // 세로 행 갯수
    int col = maps[0].size(); // 가로 열 갯수
    int sx, sy;
    bool toLever = true; // 레버로 가는 중인지

    vector<vector<int>> count (row, vector<int>(col, -1)); // 최단거리 저장할 벡터

    // 시작점 저장
    for (int i=0; i<row; i++) {
        for (int j=0; j<col; j++) {
            if (maps[i][j] == 'S') {
                sx = i;
                sy = j;
                count[i][j] = 0;
                break;
            }
        }
    }

    int startToLever = BFS(sx, sy, maps, count, row, col, true);
    int LeverToEnd = BFS(lx, ly, maps, count, row, col, false);

    answer = startToLever + LeverToEnd;
    return answer;
}