import sys
input = sys.stdin.readline

# 시간을 'HH:MM' 형식에서 분으로 변환하는 함수
def time_to_minutes(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

# 시작, 끝, 스트리밍 종료 시간 입력
S, E, Q = input().split()
S = time_to_minutes(S)
E = time_to_minutes(E)
Q = time_to_minutes(Q)

# 참가자 정보를 기록할 딕셔너리 (중복된 이름 처리 시 효율적 관리 위해 set 사용)
info = set()
cnt = 0

# 채팅 기록 처리
while True:
    try:
        log = input().split()
        if len(log) == 0:  # 빈 입력이 들어오면 종료
            break

        T = time_to_minutes(log[0])
        N = log[1]

        # 출석 체크
        if T <= S:
            info.add(N)
        # 퇴장 체크
        elif E <= T <= Q:
            if N in info:
                cnt += 1
                info.remove(N)  # 중복 카운팅 방지를 위해 제거
    except:
        break

# 결과 출력
print(cnt)

# EOF 처리 방법을 잘 몰랐다.
# 종료 조건이 안보이면 빈 입력 들어오면 종료 (try..except)

