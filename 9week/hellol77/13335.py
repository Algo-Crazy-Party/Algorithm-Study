import sys

n,w,l = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

bridge = [0] * w
answer=0

while bridge :
    answer +=1
    bridge.pop(0)

    if  arr:
        if sum(bridge)+arr[0] <=l:
            bridge.append(arr.pop(0))
        else:
            bridge.append(0)
print(answer)
