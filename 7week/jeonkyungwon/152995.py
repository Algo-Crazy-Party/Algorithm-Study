def solution(scores):
    # 1. 자 일단 완호보다 점수 합이 큰 애들을 찾아
    # 2. 그리고 걔네들 중에 인센티브 지급 가능 여부를 찾아
    #    근태 점수 최대 값이랑 동료 평가 점수 최대값을 찾아서
    #    그 수보다 둘 다 작은 애들 찾는거지
    # 3. 그렇게 걸러네고 남은 애들 수 + 1 하면 정답~
    answer = 0
    istive = [scores[0]]
    # 1.
    for people in scores:
        if sum(people) > sum(scores[0]):
            istive.append(people)
    # 2.
    m1, m2 = max
    
    return answer