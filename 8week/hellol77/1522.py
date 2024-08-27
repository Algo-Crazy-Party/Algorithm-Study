import sys

s=sys.stdin.readline().strip()
aCount = s.count('a')

s+=s[0:aCount-1]
answer = float('inf')


for i in range(len(s)-(aCount-1)):
    answer = min(answer,s[i:i+aCount].count('b'))

print(answer)
