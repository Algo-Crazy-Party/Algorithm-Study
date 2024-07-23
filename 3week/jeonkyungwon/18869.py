from collections import defaultdict
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
universe = defaultdict(int)

for _ in range(m):
    planets = list(map(int, input().split()))
    sortedPlanets = sorted(list(set(planets)))

    # 행성 순위 지정
    rank = {sortedPlanets[i]: i for i in range(len(sortedPlanets))}

    # 입력 받은 행성에 맞게 순위 저장
    vector = tuple([rank[i] for i in planets])

    # 해당 순위 벡터에 대한 개수 추가
    universe[vector] += 1

sum = 0

for i in universe.values():
    # n개 중 2개의 우주를 엮어야 하기 때문에 n C 2 를 해줘야 함 (중복 제외)
    sum += (i * (i - 1)) // 2

print(sum)