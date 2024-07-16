#include <iostream>
#include <vector>
using namespace std;

int R, C, T;
vector<vector<int>> map;

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

void spreadDust() {
    vector<vector<int>> tempMap;
    tempMap.resize(C, vector<int>(R, 0));

    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            if (map[i][j] > 0) {
                int spread = map[i][j] / 5; // 5로 나눈 몫
                int cnt = 0;
                for (int k = 0; k < 4; k++)
                {
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    if (nx >= 0 && nx < R && ny >= 0 && ny < C && map[nx][ny] != -1) {
                        tempMap[nx][ny] += spread;
                        cnt++; // 확산된 칸 수
                    }
                }
                tempMap[i][j] += (map[i][j] - spread * cnt);
            }
        }
    }

    map.swap(tempMap);
}

void airCleaner() {

}

int main() {
    cin >> R >> C >> T;

    map.resize(C, vector<int>(R, 0));
    vector<pair<int,int>> airCleanerIdx;

    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            int temp;
            cin >> temp;
            map[i][j] = temp;
            if (temp == -1) {
                airCleanerIdx.push_back({i, j});
            }
        }
    }

    for (int i = 0; i < T; i++)
    {
        spreadDust();
        airCleaner();
    }

    int dust = 0;
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            dust += map[i][j];
        }
    }
    cout << dust << '\n';
    
    return 0;
}