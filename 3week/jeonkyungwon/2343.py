import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lengths = list(map(int, input().split()))
start, end = max(lengths), sum(lengths)

def count_blurays(max_size):
    count = 1
    current_sum = 0

    for length in lengths:
        if current_sum + length > max_size:
            count += 1
            current_sum = length
        else:
            current_sum += length

    return count

while start <= end:
    mid = (start + end) // 2
    needed_blurays = count_blurays(mid)

    if needed_blurays <= M:
        end = mid - 1
    else:
        start = mid + 1

print(start)