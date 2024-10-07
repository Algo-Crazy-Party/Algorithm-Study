import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    
    for _ in range(n):
        w = heapq.heappop(works) + 1
        heapq.heappush(works, w)
    
    return sum([w ** 2 for w in works])