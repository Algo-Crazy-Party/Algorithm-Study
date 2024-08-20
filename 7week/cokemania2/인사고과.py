# https://school.programmers.co.kr/learn/courses/30/lessons/152995

def solution(scores):
    answer = 0
    target = scores[0] 
    target_score = sum(scores[0])
    
    max_b = 0
    scores.sort(key = lambda x: (-x[0], x[1]))
    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        
        if score[1] >= max_b:
            max_b = score[1]
            if target_score < sum(score):
                answer += 1
    
    return answer + 1
