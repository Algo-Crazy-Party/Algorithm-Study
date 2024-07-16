import sys

p,m = map(int,sys.stdin.readline().split())
arr=[]
for i in range(p):
    l,n = map(str,sys.stdin.readline().split())
    l = int(l)
    flag=1
    for j in range(len(arr)):
        if len(arr)==0:
            arr[0].append([[l,n]])
            flag=0
            break
        elif arr[j][0][0]-10<= l <=arr[j][0][0]+10 and len(arr[j])!=m:
            arr[j].append([l,n])
            flag=0
            break
    if flag==1:
        arr.append([[l,n]])


for i in range(len(arr)):
    if len(arr[i])==m:
        print("Started!")
    else:
        print("Waiting!")

    arr[i].sort(key=lambda x:x[1])

    for j in arr[i]:
        print(j[0] ,j[1])
