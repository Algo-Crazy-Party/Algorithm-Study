def solution(n, works):
    answer = 0

    if sum(works) <= n:
        return 0 

    works.sort(reverse = True)


    for i in range(n):
        m = max(works)

        j = 0

        while(1):
            if works[j] != m:
                break 

            works[j] -= 1
            n -= 1
            j += 1

            if n == 0:
                break

        if n == 0:
            break 

    for work in works:
        answer += (work * work)

    return answer