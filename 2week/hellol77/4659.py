import sys
checkVarr = ['a','e','i','o','u']
while 1:
    check1 = 0
    check2 = 0
    check3 = 0
    string = sys.stdin.readline().strip()
    if string=='end':
        break


    for i in range(0,len(string)):
        if string[i] in checkVarr:
            check1=1
            break
    if len(string)<3:
        check2=1
    for i in range(0,len(string)-2):
        if len(string)<3:
            check2=1
            break
        if string[i] in checkVarr and string[i+1] in checkVarr and string[i+2] in checkVarr :
            check2=0
            break
        elif string[i] not in checkVarr and string[i+1] not in checkVarr and string[i+2] not in checkVarr :
            check2=0
            break
        check2=1
    if len(string)<2:
        check3=1
    for i in range(0,len(string)-1):
        if len(string)<2:
            check3=1
            break
        if string[i]==string[i+1]:
            if string[i]=='e' or string[i]=='o':
                check3=1
            else:
                check3=0
                break
        else :
            check3=1
    if check1 ==1 and check2==1 and check3==1:
        print('<'+string+'>'+' is acceptable.')
    else:
        print('<'+string+'>'+' is not acceptable.')
