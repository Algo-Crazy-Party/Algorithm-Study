def solution(s):
    letters = ['zero','one','two','three','four','five','six','seven','eight','nine']
    answer=''
    temp=''
    for i in s:
        if i.isdigit():
            answer+=i
            continue
        else:
            temp+=i
            for index,j in enumerate(letters):
                if temp == j:
                    answer+=str(index)
                    temp=''
                    continue

    return int(answer)
