# 성격유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def set_dict(a, b, dic):
    dic[a] = b
    dic[b] = a
    
def get_win(a, b, dic):
    if dic[a] > dic[b]:
        return a
    elif dic[a] == dic[b]:
        return a if a < b else b
    return b

def solution(survey, choices):
    answer = ''
    
    score_dict = dict()
    for c in list('RTCFJMAN'):
        score_dict[c] = 0
    
    for sv, cho in zip(survey, choices):
        if cho <= 3:
            score_dict[sv[0]] += (4 - cho)
        elif cho >= 5:
            score_dict[sv[1]] += (cho - 4)
    
    answer += get_win('R', 'T', score_dict)
    answer += get_win('C', 'F', score_dict)
    answer += get_win('J', 'M', score_dict)
    answer += get_win('A', 'N', score_dict)
    
    return answer