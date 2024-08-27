import sys
import math
x,y = map(int,sys.stdin.readline().split())
answer=math.trunc((y*100)/x)
left = 0
right = x
count=x
if answer >=99:
    print(-1)
else:
    while left<=right:
        mid = (left+right)//2
        if math.trunc((y+mid)*100/(x+mid))>answer:
            count=mid
            right=mid-1
        else:
            left=mid+1

    print(count)
