import sys

s, e, q = input().split()
lines = sys.stdin.readlines()
attendance_dict = dict()
answer_set = set()
for line in lines:
    time, nickname = line.split()
    if (e <= time <= q) and (nickname in attendance_dict):
        answer_set.add(nickname)
    
    # 개강총회에 참석했으면 추가
    if time <= s:
        attendance_dict[nickname] = time
print(len(answer_set))