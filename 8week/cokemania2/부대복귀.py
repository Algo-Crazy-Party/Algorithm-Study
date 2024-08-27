from collections import deque

def create_map_dict(n):
    """
    모든 맵 정보를 -1로 초기화하여 딕셔너리를 생성
    """
    return {i: -1 for i in range(1, n + 1)}

def save_short_cuts(destination, map_dict, road_dict):
    """
    BFS 방식으로 최단 거리를 계산하여 딕셔너리에 저장
    도달하는 지역이 -1(미방문)이거나 더 빨리 방문 가능하면 진행
    """
    queue = deque([[destination, 0]])
    
    while queue:
        road, count = queue.popleft()
        if map_dict[road] == -1 or map_dict[road] > count:
            map_dict[road] = count
        
            next_roads = road_dict[road]
            for next_road in next_roads:
                queue.append([next_road, count + 1])
            

def road_to_dict(a, b, dic):
    """
    경로 정보를 dict로 변환
    """
    if a in dic:
        dic[a].append(b)
    else:
        dic[a] = [b]

def solution(n, roads, sources, destination):
    answer = []
    road_dict = dict()
    
    for road in roads:
        road_to_dict(road[0], road[1], road_dict)
        road_to_dict(road[1], road[0], road_dict)
    
    map_dict = create_map_dict(n)
    save_short_cuts(destination, map_dict, road_dict)
    
    for source in sources:
        answer.append(map_dict[source])
    
    return answer