# https://school.programmers.co.kr/learn/courses/30/lessons/77885
# 2개 이하로 다른 비트

def solution(numbers):
    """
    짝수는 10으로 끝나기 때문에 + 1 처리
    홀수는 뒤부터 0을 1로 바꾸면 break
    """
    answer = []
    
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            binary = list(bin(number)[2:])
            binary.reverse()
            
            for i in range(len(binary)):
                if binary[i] == '0':
                    binary[i] = '1'
                    break
                else:
                    binary[i] = '0'
            
            binary.reverse()
            answer.append(int(''.join(binary), 2))
    
    return answer