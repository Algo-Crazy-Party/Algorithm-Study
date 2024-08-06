import heapq

def solution(book_time):
    arr=[]
    for a,b in book_time:
        a=int(a.split(':')[0])*60 + int(a.split(':')[1])
        b=int(b.split(':')[0])*60 + int(b.split(':')[1])+10
        arr.append([a,b])
    arr.sort()
    room=[]
    heapq.heappush(room,arr[0][1])

    for i in range(1,len(arr)):
        if room[0]<=arr[i][0]:
            heapq.heappop(room)
            heapq.heappush(room,arr[i][1])
        else:
            heapq.heappush(room,arr[i][1])

    return len(room)
