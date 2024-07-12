"""
[ 조건 ]
공통: 문자를 두개 포함해야함
1: 가장 짧은 연속 문자열
2: 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이

[ 풀이 ]
- 각 문자(a ~ z)별 이중 리스트를 만들기
- index를 기록, 기록과 동시에 최소 간격 계산
- 기록을 모두 마친 후 최장 간격 계산
"""

def longest_index_diff(index_list):
    return index_list[-1] - index_list[-k] + 1

def shortest_index_idff(index_list, k):
    return index_list[-1] - index_list[-k] + 1


t = int(input())
answer = []
for i in range(t):
    w = list(input())
    k = int(input())

    alpha_list = [[] for _ in range(29)]
    shortest_min_length = 10001
    longest_max_length = -1
    for j, v in enumerate(w):
        alpha_index = ord('a') - ord(v)
        alpha_list[alpha_index].append(j)
        if len(alpha_list[alpha_index]) >= k:
            shortest_min_length = min(shortest_min_length, shortest_index_idff(alpha_list[alpha_index], k))
            longest_max_length = max(longest_max_length, longest_index_diff(alpha_list[alpha_index]))

    answer.append([shortest_min_length, longest_max_length])

for i in range(t):
    if answer[i][0] == 10001 or answer[i][1] == -1:
        print("-1")
    else:
        print(answer[i][0], answer[i][1])
