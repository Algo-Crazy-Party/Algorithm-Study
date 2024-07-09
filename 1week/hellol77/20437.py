import sys
from collections import defaultdict

t=int(sys.stdin.readline())

for i in range(t):
    firstAnswer=sys.maxsize
    secondAnswer=0
    w=sys.stdin.readline().strip()
    k = int(sys.stdin.readline())
    position=defaultdict(list)

    for index,ww in enumerate(w):
        position[ww].append(index)


    for char, positionList in position.items():
        if len (positionList)<k:
            continue
        for i in range(len(positionList) - k +1):
            length = positionList[i+k-1] - positionList[i]+1
            firstAnswer = min(firstAnswer,length)
            secondAnswer = max(secondAnswer,length)
    if firstAnswer ==sys.maxsize and secondAnswer == 0:
        print(-1)
    else:
        print(firstAnswer,secondAnswer)
