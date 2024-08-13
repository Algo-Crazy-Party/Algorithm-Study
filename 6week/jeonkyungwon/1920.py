from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
dict = defaultdict(int)

for i in A:
    dict[i] = 1

for i in B:
    print(1) if dict[i] > 0 else print(0)