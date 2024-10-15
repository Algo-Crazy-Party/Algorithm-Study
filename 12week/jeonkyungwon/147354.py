def solution(data, col, row_begin, row_end):
    answer = 0
    # 나중을 위해 먼저 첫 번째 칼럼의 값으로 내림차정렬
    data.sort(reverse = True)
    # col번 째 칼럼의 값을 기준으로 오름차순 정렬 
    data.sort(key = lambda x: x[col - 1])
    
    # 범위 내의 값들 순회
    for i in range(row_begin - 1, row_end):
        S = 0
        # i로 나눈 값들 S에 더해주기
        for j in range(0, len(data[i])):
            S +=  data[i][j] % (i + 1)
        # XOR 연산
        answer ^= S
        
    return answer

# XOR 연산을 파이썬에서 어떻게 하는지 몰랐다.
# 잘 알아두자.