from collections import deque

def solution(priorities, location):
    m = max(priorities)
    temp = []
    for index,i in enumerate(priorities):
        temp.append([i,index])
    d = deque(temp)
    result = []
    while d:
        if d[0][0]==m:
            result.append(d.popleft())
            if d:
                max_0=max(d, key=lambda x: x[0])
                m=max_0[0]
        else:
            d.append(d.popleft())


    for index,i in enumerate(result):
        if i[1]==location:
            return index+1
