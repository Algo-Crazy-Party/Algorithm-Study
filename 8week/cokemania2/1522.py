# https://www.acmicpc.net/problem/1522
# 문자열 교환

# 문제 이해하기 어려움

s = input()
length = len(s)
a_count = s.count('a')
min_count = length

s += s[:a_count]

for i in range(length):
    min_count = min(min_count, s[i:i+a_count].count('b'))

print(min_count)