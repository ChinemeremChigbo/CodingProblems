from bisect import insort
def evaluate(days,evalList,cap):
    dp = [0]*(days)
    start = [b for a,b,c in evalList]
    current = [[] for i in range(days)]
    for a,b,c in evalList:
        for k in range(b-1,c):
            insort(current[k],(a))
    for i in start:
        dp[i-1] = sum(current[i-1][-cap:])
    return max(dp)
t = int(input())
for i in range(t):
    days,attractions,cap = [int(i) for i in input().split()]
    evalList = []
    for j in range(attractions):
        a,b,c = [int(i) for i in input().split()]
        evalList.append([a,b,c])
    print("Case #",end="")
    print(str(i+1)+": "+str(evaluate(days,evalList,cap)))