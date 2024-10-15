def imPossible(result):
    for x,y,a in result:
        if a==0: # 기둥일 때
            if y != 0 and (x,y-1,0) not in result and (x-1,y,1) not in result and (x,y,1) not in result:
                return True
        else:    # 보일 때
            if (x,y-1,0) not in result and (x+1,y-1,0) not in result and not((x-1,y,1) in result and (x+1,y,1) in result):
                return True
    return False

def solution(n, build_frame):
    answer=set()

    for x,y,a,build in build_frame:
        item = (x,y,a)
        if build:
            answer.add(item)
            if imPossible(answer):
                answer.remove(item)
        elif item in answer:
            answer.remove(item)
            if imPossible(answer):
                answer.add(item)
    answers = map(list,answer)
    return sorted(answer,key=lambda x :(x[0],x[1],x[2]))
