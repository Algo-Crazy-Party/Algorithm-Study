# https://www.acmicpc.net/problem/1141
# 접두사

# 문자 순서대로 정렬, 같다면 길이 순으로 정렬
# 앞 단어가 뒷 단어의 접두사가 되면 continue
# 그렇지 않다면 answer += 1

words = []
n = int(input())
for i in range(n):
    words.append(input())

words.sort(key=lambda x: (x, len(x)))

answer = 0
for i in range(1, len(words)):
    if words[i].startswith(words[i-1]):
       continue
    answer += 1

print(answer + 1)