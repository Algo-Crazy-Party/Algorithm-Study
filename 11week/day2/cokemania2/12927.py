# https://school.programmers.co.kr/learn/courses/30/lessons/12927
# 야근 지수

# 문제 이해 어려움
# 모든 수를 even하게 익힌다.

def _pow(n):
    return n * n

def solution(n, works):
    answer = 0
    
    works.sort(reverse=True)
    
    while True:
        maxx = works[0]
        if maxx <= 0:
            break
        for i in range(len(works)):
            if n <= 0:
                break
            if works[i] >= maxx:
                works[i] -= 1
                n -= 1
            else:
                break
        
        if n <= 0:
            break
    return max(sum(list(map(_pow, works))), 0)
