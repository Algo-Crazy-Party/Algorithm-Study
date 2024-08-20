import sys
from collections import defaultdict
n,k = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

answer=0

start,end=0,0
countDict = defaultdict(int)


while end<n:
    if countDict[arr[end]]>=k:
        countDict[arr[start]]-=1
        start+=1
    else:
        countDict[arr[end]]+=1
        end+=1
        answer=max(answer,end-start)
print(answer)
