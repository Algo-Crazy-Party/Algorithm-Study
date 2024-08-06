def solution(k, m, score):
    score.sort(reverse=True)
    answer=0
    for i in range(len(score)//m):
        minNumber=min(score[0+m*i:m+m*i])
        answer+=minNumber*m


    return answer
