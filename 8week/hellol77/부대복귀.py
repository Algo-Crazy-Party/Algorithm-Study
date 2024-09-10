from collections import deque

def solution(n, roads, sources, destination):
    visited = [-1]*(n+1)
    graph = [[] for i in range(n+1)]

    for s ,e in roads:
        graph[s].append(e)
        graph[e].append(s)

    q = deque([destination])
    visited[destination]=0
    while q:
        now = q.popleft()

        for i in graph[now]:
            if visited[i]==-1:
                visited[i] = visited[now]+1
                q.append(i)
    return [visited[i] for i in sources]
