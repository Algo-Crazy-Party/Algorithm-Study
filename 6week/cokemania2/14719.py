# https://www.acmicpc.net/problem/14719

# 끝 벽이 안막혀 있을경우 0
# left_wall, right_wall

h, w = map(int, input().split())
w_list = list(map(int, input().split()))

answer = 0
for i in range(1, w-1):
    left_wall = max(w_list[:i])
    right_wall = max(w_list[i+1:])

    minimum = min(left_wall, right_wall)
    if w_list[i] < minimum:
        answer += minimum - w_list[i]

print(answer)