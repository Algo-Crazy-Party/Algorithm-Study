#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<vector<int>> makeGraph(int n, vector<vector<int>> roads) {
    vector<vector<int>> graph(n);
    for(auto& road: roads) {
        int u = road[0];
        int v = road[1];
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    
    return graph;
}

int BFS(int start, int dest, vector<vector<int>> graph) {
    vector<int> dist(graph.size(), -1);
    queue<int> q;
    
    q.push(start);
    dist[start] = 0;
    
    while (!q.empty()) {
        int current = q.front();
        q.pop();
        
        for (int n: graph[current]) {
            if (dist[n] == -1) {
                q.push(n);
                dist[n] = dist[current] + 1;
                
                if (n == dest) {
                    return dist[n];
                }
            }
        }
    }
    
    return -1;
}

vector<int> solution(int n, vector<vector<int>> roads, vector<int> sources, int destination) {
    vector<int> answer;
    vector<vector<int>> graph = makeGraph(n, roads);
    
    for(int s: sources) {
        // s -> dest 그래프 최단거리
        int result = BFS(s, destination, graph);
        answer.push_back(result);
    }
    
    return answer;
}