# https://www.acmicpc.net/problem/13335
# 트럭

# 트럭의 수, 다리의 길이, 다리의 최대 하중
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w
time = 0
while trucks:
    time += 1
    bridge.pop(0)
    if sum(bridge) + trucks[0] <= l:
        bridge.append(trucks.pop(0))
    else:
        bridge.append(0)
print(time + w)
