import sys
from collections import deque
testcase=int(sys.stdin.readline())

for i in range(testcase):
    n,m = map(int,sys.stdin.readline().split())
    l = list(map(int,sys.stdin.readline().split()))
    tempMax=max(l)
    temp=[]
    for index,j in enumerate(l):
        temp.append([j,index])
    d = deque(temp)
    result = []
    while d:
        if d[0][0]==tempMax:
            result.append(d.popleft())
            if d:
                tempMax = max(d,key=lambda x:x[0])[0]
        else:
            d.append(d.popleft())
    for index,k in enumerate(result):
        if k[1]==m:
            print(index+1)
