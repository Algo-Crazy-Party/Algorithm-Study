# from math import log2
# import sys
# import heapq
# input = sys.stdin.readline

# N, K = map(int, input().split())

# current = []

# while True:
#     if(N <= 1):
#         heapq.heappush(current, 1)
#         break
#     num = 2 ** int(log2(N))
#     heapq.heappush(current, num)
#     N -= num

# print(current)
# count = 0

# while len(current) > K :
#     if(not current):
#         break
#     first = heapq.heappop(current)
#     second = heapq.heappop(current)

#     if(first == second):
#         heapq.heappush(current, first + second)
#     else:
#         count += second - first
#         heapq.heappush(current, second+first)


# if count == 0:
#     print(-1)
# else:
#     print(count)




from math import log2
import sys
import heapq
import math
input = sys.stdin.readline

N, K = map(int, input().split())

if N < K:
    print(0)
    exit()
current = []
answer=0
while N:
    # if(N <= 1):
    #     current.append(1)
    #     break

    num = 2 ** math.trunc(log2(N))
    current.append(num)
    N -= num

while len(current) > K:
    temp=float("inf")
    firstValue=-1
    secondValue=-1
    for i in range(len(current)):
        for j in range(i+1,len(current)):
            if abs(current[j]-current[i]) <temp:
                firstValue = current[i]
                secondValue= current[j]
                temp= abs(secondValue-firstValue)
    answer+=temp
    if secondValue > firstValue:
        current.append(secondValue*2)
    else:
        current.append(firstValue*2)
    current.remove(firstValue)
    current.remove(secondValue)
print(answer)
