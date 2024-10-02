import sys

n=int(sys.stdin.readline())
answer=0
arr=[]
for i in range(n):
    s = sys.stdin.readline().strip()
    arr.append(s)

arr.sort(key=len)
for i in range(n):
    flag =0
    for j in range(i+1,n):
        if arr[i]==arr[j][0:len(arr[i])]:

            flag=1
            break
    if flag ==0:
        answer+=1
print(answer)
