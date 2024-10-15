from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # 두 큐의 합을 미리 계산
    sum1 = sum(q1)
    sum2 = sum(q2)
    total = sum1 + sum2
    
    # 총합이 홀수면 두 큐를 같게 만들 수 없음
    if total % 2 != 0:
        return -1
    
    # 목표로 하는 각 큐의 합
    target = total // 2
    
    cnt = 0
    limit = len(q1) + len(q2) * 2
    
    # 투포인터처럼 두 큐를 비교하면서 진행
    while sum1 != target and cnt <= limit:
        if sum1 > target:
            # q1의 합이 크면 q1에서 하나를 빼서 q2에 넣음
            value = q1.popleft()
            q2.append(value)
            sum1 -= value
        else:
            # q2의 합이 크면 q2에서 하나를 빼서 q1에 넣음
            value = q2.popleft()
            q1.append(value)
            sum2 -= value
            sum1 += value
        cnt += 1
    
    # 결과 확인
    if sum1 == target:
        return cnt
    else:
        return -1
    
    # 큐의 합을 미리 계산 안했다고 시간 초과가 날 줄은 몰랐다
    # 결론적으로 두 큐 중에 총 합이 더 큰 쪽에서 이동시키는 방법으로 해결 가능
    # 어떤 두 무언가의 합이 같아져야하는 문제에서 잘 생각하기