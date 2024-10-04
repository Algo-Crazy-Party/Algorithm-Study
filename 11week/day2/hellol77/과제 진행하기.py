def solution(plans):
    answer=[]
    stack=[]
    for index in range(len(plans)): # 시간을 분으로 바꾸기
        temp=plans[index][1]
        hour,minute=map(int,temp.split(':'))
        time=hour*60+minute
        plans[index][1]=time
        plans[index][2]=int(plans[index][2])
    plans.sort(key=lambda x:x[1])
    for i in range(len(plans)):
        if i ==len(plans)-1: # 마지막 과제는 바로 stack에 넣어준다.
            stack.append(plans[i])
            break
        sub,start,t=plans[i]
        nsub,nstart,nt=plans[i+1]
        if start+t<=nstart: # 다음 과제 시작 시간 보다 이전 과제 시작시간 + 이전 과제 걸리는 시간 이 작아서 이전 과제를 끝낼 수 있는 경우
            answer.append(sub)
            tempTime=nstart-(start+t) # 다음 과제시작 시간 - (이전 과제 시작시간+이전 과제 걸리는 시간) 무조건 양수가 된다
            while tempTime!=0 and stack: # stack이 있고 tempTime이 0이 아닐때
                tsub, tst, tt=stack.pop() # 다 끝내지 못한 과제
                if tempTime>=tt: # 이전 과제를 끝낸후 남은 시간에 못한과제를 끝낼 수 있는 경우
                    answer.append(tsub)
                    tempTime-=tt
                else:
                                # 이전 과제를 끝낸후 남은 시간에 못한과제를 못 끝내는 경우
                    stack.append([tsub, tst,tt-tempTime]) # 남은 시간동안 끝내지 못한 과제를 한 후 다시 다 끝내지 못한 과제목록으로 넣는다
                    tempTime=0                              # 남은 시간을 다 썼으므로 0으로 초기화
        else: # 이전 과제를 못 끝내는 경우
            plans[i][2]=t-(nstart-start)
            stack.append(plans[i])
    while stack:
        sub, start,t=stack.pop() # 멈춰둔 과제가 여러 개인 경우 최근에 멈춘 과제부터 시작한다. 그래서 stack 을 이용하는 것 같다.
        answer.append(sub)
    return answer
