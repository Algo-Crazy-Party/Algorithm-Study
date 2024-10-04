# https://school.programmers.co.kr/learn/courses/30/lessons/176962
# 과제 진행하기

def time_to_minute(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)

def do_remain_plan(done, remain, remain_time):
    while len(remain) and remain_time:
        remain_plan = remain.pop()
        if remain_plan[2] <= remain_time:
            done.append(remain_plan)
            remain_time -= remain_plan[2]
        else:
            remain_plan[2] -= remain_time
            remain.append(remain_plan)
            remain_time = 0

def do_plan(i, plans, done, remain):
    if i == len(plans) - 1:
        done.append(plans[i])
        do_remain_plan(done, remain, 60 * 60 * 100 * 24)
        return 
    
    now_plan = plans[i]
    next_plan = plans[i + 1]
    
    end_time = time_to_minute(now_plan[1]) + int(now_plan[2])
    next_plan_start_time = time_to_minute(next_plan[1])

    if end_time > next_plan_start_time:
        now_plan[2] = end_time - next_plan_start_time
        remain.append(now_plan)
    else:
        done.append(now_plan)
        remain_time = next_plan_start_time - end_time
        do_remain_plan(done, remain, remain_time)


def solution(plans):
    done = []
    remain = []
    plans.sort(key = lambda x : x[1])
    for i in range(len(plans)):
        do_plan(i, plans, done, remain)
    
    return [d[0] for d in done]