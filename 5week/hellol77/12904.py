import sys

s=list(sys.stdin.readline().strip())

t=list(sys.stdin.readline().strip())

while len(t)>=len(s):
    if t==s:
        print(1)
        exit()
    if t[-1]=='B':
        t.pop()
        t=t[::-1]
    elif t[-1]=='A':
        t.pop()

print(0)
