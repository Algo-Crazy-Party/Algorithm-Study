import sys
input = sys.stdin.readline

s = input().strip()
count_a = s.count('a')

if count_a == 0:
    print(0)
    exit()

s = s + s
min_b_count = float('inf')
current_b_count = s[:count_a].count('b')
min_b_count = min(min_b_count, current_b_count)

for i in range(1, len(s) // 2):
    if s[i - 1] == 'b':
        current_b_count -= 1

    if s[i + count_a - 1] == 'b':
        current_b_count += 1

    min_b_count = min(min_b_count, current_b_count)

print(min_b_count)