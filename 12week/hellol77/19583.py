import sys

S,E,Q = map(str,sys.stdin.readline().split())

sTime = int(S[:2])*60+int(S[3:])
eTime = int(E[:2])*60+int(E[3:])
qTime = int(Q[:2])*60+int(Q[3:])

s=set()
answer=0

while True:
    try:
        time,name=map(str,sys.stdin.readline().split())
        time = int(time[:2])*60+int(time[3:])
        if time <=sTime:
            s.add(name)
        elif eTime<=time<=qTime and name in s:
            s.remove(name)
            answer+=1
    except:
        break
print(answer)
