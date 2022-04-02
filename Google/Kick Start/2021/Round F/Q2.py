# from bisect import insort
# def evaluate(days,evalList,cap):
#     dp = [0]*(days)
#     start = [b for a,b,c in evalList]
#     current = [[] for i in range(days)]
#     for el in start:
#         for a,b,c in evalList:
#             if b <= el <= c :
#                 insort(current[el-1],a)
#     for i in start:
#         dp[i-1] = sum(current[i-1][-cap:])
#     print(current,dp)
#     return max(dp)
# t = int(input())
# for i in range(t):
#     days,attractions,cap = [int(i) for i in input().split()]
#     evalList = []
#     for j in range(attractions):
#         a,b,c = [int(i) for i in input().split()]
#         evalList.append([a,b,c])
#     print("Case #",end="")
#     print(str(i+1)+": "+str(evaluate(days,evalList,cap)))

