# https://school.programmers.co.kr/learn/courses/30/lessons/150367
# 표현 가능한 이진트리

# 포화 이진트리: 빈곳이 없이 꽉 찬 이진트리
# 포화 이진트리 특징 
# - 1, 3, 7, 15 ... (노드의 수가 1 + 2의 제곱 만큼 늘어남)
# 기존 이진수에 앞에 0을 포화 이진 수가 될만큼 붙임


def add_dummy(bin_num):
    # 기존 이진수에 앞에 0을 포화 이진 수가 될만큼 붙임
    i = 1
    while (2 ** i - 1) < len(bin_num):
        i += 1
    for _ in range(2 ** i - 1 - len(bin_num)):
        bin_num = '0' + bin_num
    return bin_num

def is_right_dummy(root_node, bin_num):
    if len(bin_num) == 1:
        return not (root_node == '0' and bin_num[0] == '1')
    
    mid = len(bin_num) // 2
    # (root_node가 0 이고 현재 노드가 1)이 아니면 OK
    if root_node == '0' and bin_num[mid] == '1':
        return False

    
    # 루트노드를 기준으로 노드의 왼쪽 오른쪽 검사
    
    return is_right_dummy(bin_num[mid], bin_num[:mid]) and is_right_dummy(bin_num[mid], bin_num[mid + 1:])

def can_full_binary(bin_num):
    # 노드의 길이가 1일경우
    if len(bin_num) == 1:
        return True
    
    # 포화 이진트리가 될때까지 더미 노드를 더해준다.
    bin_num = add_dummy(bin_num)
    
    # 첫 루트노드가 0일경우 False
    if bin_num[len(bin_num) // 2] == '0':
        return False
    
    return is_right_dummy('1' , bin_num)
    
    
def solution(numbers):
    answer = []
    
    for number in numbers:
        bin_num = bin(number)[2:]
        if can_full_binary(bin_num):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer