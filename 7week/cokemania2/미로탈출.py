from collections import deque

def find_S_E_L(maps):
    answer = [() for _ in range(3)]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                answer[0] = (i, j)
            elif maps[i][j] == "E":
                answer[1] = (i, j)
            elif maps[i][j] == "L":
                answer[2] = (i,j)
    return answer
        
def cost_find_target(maps, start, end, cost):
    queue = deque([[start[0], start[1], cost]])
    visited = set([start])
    while queue:
        y, x, c = queue.popleft()
        if (y, x) == end:
            return c
        for dy, dx in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] != "X" and (ny, nx) not in visited:
                queue.append((ny, nx, c + 1))
                visited.add((ny, nx))
    return -1
    
    
def solution(maps):
    s, e, l = find_S_E_L(maps)
    x = cost_find_target(maps, s, l, 0)
    x2 = cost_find_target(maps, l, e, 0)
    
    return x + x2 if x != -1 and x2 != -1 else -1

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))