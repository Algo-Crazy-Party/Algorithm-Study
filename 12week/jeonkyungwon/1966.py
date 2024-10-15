from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    # 중요도를 deque로 설정
    N, M = map(int, input().split())
    IM = deque(map(int, input().split()))
    cnt = 0

    # 모든 문서가 인쇄되기 전까지
    while IM:
        # 자신보다 중요도가 큰 문서가 있으면 맨 뒤로 
        if max(IM) > IM[0]:
            IM.append(IM.popleft())
            # 몇 번째로 인쇄되는지 알고 싶은 M 값 앞으로 밀기
            if M == 0:
                M = len(IM)
            M -= 1
        # 자신의 중요도보다 큰 문서가 없으면 인쇄
        else:
            IM.popleft()
            # 인쇄 횟수 체크
            cnt += 1
            # 몇 번째로 인쇄되는지 알고 싶은 M이 0이 되면 인쇄되었다는 뜻이므로 정지
            M -= 1
            if M < 0:
                break

    print(cnt)