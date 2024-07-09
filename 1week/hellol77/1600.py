import sys
from collections import deque
k = int(sys.stdin.readline())

w,h=map(int,sys.stdin.readline().split())
arr=[]
visited = [[0 for i in range(w)] for i in range(h)]
for i in range(h):
    arr.append(list(map(int,sys.stdin.readline().split())))
answer=sys.maxsize

normalMoves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
knightMoves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

def bfs(x,y,k):
    q=deque()
    visited = [[[0 for i in range(k+1)] for i in range(w)] for i in range(h)]
    visited[x][y][k]=1
    q.append((x,y,k,0))
    if x==h-1 and y==w-1:
        return 0
    while q:
        xx,yy,kk,nn = q.popleft()
        if xx==h-1 and yy==w-1:
            return nn

        for dx,dy in normalMoves:
            nx=dx+xx
            ny=dy+yy
            if 0 <=nx < h and 0 <=ny <w and  visited[nx][ny][kk]==0 and arr[nx][ny] == 0:
                visited[nx][ny][kk]=1
                q.append((nx,ny,kk,nn+1))
        if kk>0:
            for dx,dy in knightMoves:
                nx= dx+xx
                ny=dy+yy
                if 0 <=nx < h and 0 <=ny <w and  visited[nx][ny][kk-1]==0 and arr[nx][ny] == 0:
                    visited[nx][ny][kk-1]=1
                    q.append((nx,ny,kk-1,nn+1))

    return -1
print(bfs(0,0,k))
