def solution(survey, choices):
    answer=[]

    dic=dict.fromkeys(('R,T,C,F,J,M,A,N'),0)

    for index,i in enumerate(survey):
        if choices[index]==4:
            continue
        elif choices[index]>4:
            dic[i[1]]+=choices[index]-4
        elif choices[index]<4:
            dic[i[0]]+=4-choices[index]

    if dic['R']>=dic['T']:
        answer.append('R')
    elif dic['R']<dic['T']:
        answer.append('T')

    if dic['C']>=dic['F']:
        answer.append('C')
    elif dic['C']<dic['F']:
        answer.append('F')


    if dic['J']>=dic['M']:
        answer.append('J')
    elif dic['J']<dic['M']:
        answer.append('M')


    if dic['A']>=dic['N']:
        answer.append('A')
    elif dic['A']<dic['N']:
        answer.append('N')



    return ''.join(answer)
