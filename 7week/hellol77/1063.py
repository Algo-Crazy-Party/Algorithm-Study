import sys

king,stone,n = map(str,sys.stdin.readline().split())

n=int(n)

arr = [ [0 for i in range(8)] for i in range(8)]

locationDict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

# king 은 1
arr[king[1]-1][locationDict[king[0]]]=1

# stone 은 2
arr[stone[1]-1][locationDict[stone[0]]]=2

for i in range(n):
    loc = sys.stdin.readline().strip()
