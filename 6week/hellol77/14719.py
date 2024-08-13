H,W=map(int,input().split())
A=list(map(int,input().split()))
ans=0
for i in range(1,W-1):
    l=max(A[:i])
    r=max(A[i:])

    k=min(l,r)

    if A[i]<k:
        ans+=k-A[i]


print(ans)
