import sys
from collections import defaultdict

n = int(input())
n_set = set(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

dic = defaultdict(int)

for xxx in m_arr:
    if xxx in n_set:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")