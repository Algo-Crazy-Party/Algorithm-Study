# https://www.acmicpc.net/problem/1966
# 프린터 큐 


def solution(priorities, location):
    answer = 0
    x = priorities[location]
    priorities[location] = -1
    
    while len(priorities) > 0:
        flag = False
        

        v = priorities.pop(0)
        if v == -1:
            v = x
            flag = True

        if len(priorities) > 1 and v < max(priorities + [x]):
            priorities.append(v if not flag else -1)
        else:
            answer += 1
            if flag:
                break
                
    return answer

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution(arr, m))
