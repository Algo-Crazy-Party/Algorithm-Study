import sys

r,c,t = map(int,sys.stdin.readline().split())
arr=[]
answer=0

for i in range(r):
    a=list(map(int,sys.stdin.readline().split()))
    arr.append(a)

upAirloc = -1
downAirloc = -1
for i in range(r):
    if arr[i][0]==-1:
        upAirloc = i
        downAirloc = i+1
        break



def spread():
    dxs = [0,1,-1,0]
    dys = [1,0,0,-1]
    tempArr = [[0 for i in range(c)]for i in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] !=0 and arr[i][j]!=-1:
                temp=0
                for k in range(4):
                    dx = dxs[k]+i
                    dy = dys[k]+j
                    if 0<=dx<r and 0<=dy<c and arr[dx][dy]!=-1:
                        tempArr[dx][dy]+=arr[i][j]//5
                        temp+=arr[i][j]//5
                arr[i][j]-=temp

    for i in range(r):
        for j in range(c):
            arr[i][j]+=tempArr[i][j]


def upAir():
    dxs = [0,-1,0,1]
    dys = [1,0,-1,0]

    direction = 0
    x,y = upAirloc,1
    temp = 0

    while 1:
        dx = x+dxs[direction]
        dy = y+dys[direction]
        if x== upAirloc and y==0:
            break
        if  0>dx or dx>= r or  0>dy or dy >=c:
            direction+=1
            continue
        arr[x][y],temp = temp,arr[x][y]
        x=dx
        y=dy

def downAir():
    dxs = [0,1,0,-1]
    dys = [1,0,-1,0]
    direction = 0
    x,y = downAirloc ,1
    temp=0
    while 1:
        dx = x+dxs[direction]
        dy = y+dys[direction]
        if x ==downAirloc and y == 0:
            break
        if 0>dx or dx>= r or  0>dy or dy >=c:
            direction+=1
            continue
        arr[x][y],temp = temp,arr[x][y]
        x=dx
        y=dy

for i in range(t):
    spread()
    upAir()
    downAir()

for i in range(r):
    for j in range(c):
        if arr[i][j]>0:
            answer+=arr[i][j]

print(answer)
