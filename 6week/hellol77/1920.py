import sys

n=int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

m=int(sys.stdin.readline())

arr=list(map(int,sys.stdin.readline().split()))

s = set(a)
for i in arr:
    if i in s:
        print(1)
    else:
        print(0)
