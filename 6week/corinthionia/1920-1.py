# stdin.readline() - 한번에 읽어와서 버퍼에 저장
# input() - 하나씩 누를 때마다 데이터를 버퍼에 저장
from sys import stdin, stdout
input = stdin.readline

N = input()
A = set(input().split())

M = input()
nums = input().split()

for el in nums:
    stdout.write('1\n') if el in A else stdout.write('0\n')