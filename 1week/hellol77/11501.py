import sys

t=int(sys.stdin.readline())

for i in range(t):
    n=int(sys.stdin.readline())
    ns = list(map(int,sys.stdin.readline().split()))
    ns.reverse()
    answer=0
    temp=ns[0]
    for j in range(1,n):
        if temp<ns[j]:
            temp=ns[j]
        else:
            answer+=temp-ns[j]
    print(answer)
