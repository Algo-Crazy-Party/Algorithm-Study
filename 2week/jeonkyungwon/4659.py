import sys
input = sys.stdin.readline

con = ['a', 'e', 'i', 'o', 'u']

while 1:
    arr = input().rstrip()
    cnt, check = 0, 0
    a, b = 0, 0
    c = []

    if arr == 'end':
        break

    for i in range(len(arr)):
        if i < len(arr) - 1:
            if arr[i] == arr[i + 1] and (arr[i] != 'e' and arr[i] != 'o'):
                print("<", arr, "> is not acceptable.", sep='')
                check += 1
                break

        if arr[i] in con:
            cnt += 1
            a += 1
            b = 0

            if a == 3:
                print("<", arr, "> is not acceptable.", sep='')
                check += 1
                break
        else:
            b += 1
            a = 0

            if b == 3:
                print("<", arr, "> is not acceptable.", sep='')
                check += 1
                break

    if check == 0:
        if cnt == 0:
            print("<", arr, "> is not acceptable.", sep='')
        else:
            print("<", arr, "> is acceptable.", sep='')