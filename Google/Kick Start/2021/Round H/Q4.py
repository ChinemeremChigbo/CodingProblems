from fractions import Fraction
from collections import defaultdict
def func(e,q,n):
    bfs = [1]
    count = 0
    adjList = defaultdict(list)
    prob = {i:i*1000 for i in range(1,n+2)}
    for i in e:
        if i != 1:
            a,b,c = e[i]
            adjList[a].append(i)
    print(adjList,prob)
    # while bfs and count < 500:
    #     nextList = []
    #     for i in bfs:
    #         nextList.append

    #     bfs = nextList
    #     count += 1
    # events = {}
    # print(e,q)
    res = []
    
    for a,b in q:
        frac = Fraction(prob[a] * prob[b])
        res.append((frac.numerator%(10**9 + 7))//frac.denominator)
    print(" ".join(res))
    return " ".join(res)

t = int(input())

for i in range(t):
    e = {}
    q = []
    n,m = input().split()
    n,m = int(n),int(m)
    for j in range(n):
        e[j+1] = [int(k) for k in input().split()]
    for l in range(m):
        q.append([int(k) for k in input().split()])
    print("Case #" + str(i+1)+": "+str(func(e,q,n)))