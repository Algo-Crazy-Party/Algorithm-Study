import sys

m,n = map(int,sys.stdin.readline().split())
d={}
arr=[]
tempArr = [[]for i in range(m)]
answer=0
for i in range(m):
    l = list(map(int,sys.stdin.readline().split()))
    arr.append(l)


for i in range(m):
    narr=sorted(list(set(arr[i])))
    for j in range(len(narr)):
        d[narr[j]]=j
    for k in arr[i]:
        tempArr[i].append(d[k])

tempArr.sort()
count=1
for i in range(1,m):
    if tempArr[i]==tempArr[i-1]:
        count+=1
    else:
        answer+=count*(count-1)//2
        count=1
answer += count*(count-1)//2
print(answer)
