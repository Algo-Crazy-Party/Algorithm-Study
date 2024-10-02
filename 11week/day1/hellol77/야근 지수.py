import heapq

def solution(n, works):
    if n>=sum(works):
        return 0

    works = [-i for i in works]

    heapq.heapify(works)

    for i in range(n):

        k=heapq.heappop(works)
        k+=1
        heapq.heappush(works,k)

    answerArr = [i*i for i in works]

    return sum(answerArr)
