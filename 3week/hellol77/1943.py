# import sys


# for i in range(3):
#     n=int(sys.stdin.readline())
#     dp=[{0}]
#     for j in range(n):
#         money,count = map(int,sys.stdin.readline().split())
#         temp=[]
#         for a in dp[-1]:
#             for k in range(0,count+1):
#                 temp.append((a+money*k-money*(count-k)))
#         t = set(temp)
#         dp.append(t)
#     flag=0

#     dp = set(dp[-1])
#     if 0 in dp:
#         print(1)
#     else:
#         print(0)

