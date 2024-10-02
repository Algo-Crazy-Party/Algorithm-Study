def solution(survey, choices):
    types = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    answer = ''
    for i in range(len(survey)):
        if choices[i] > 4:
            types[survey[i][1]] += choices[i] % 4
        elif choices[i] < 4:
            types[survey[i][0]] += 4 - choices[i] % 4

    result = list(types.items())
    
    for i in range(len(types) // 2):
        if result[i * 2][1] >= result[i * 2 + 1][1]:
            answer += result[i * 2][0]
        else:
            answer += result[i * 2 + 1][0]
    
    return answer