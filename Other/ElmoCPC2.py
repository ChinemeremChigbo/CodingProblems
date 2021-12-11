# import SortedDict

from collections import deque

def helper(l1,l2):
    l1.sort()
    l2.sort()
    print(l1,l2)
    for i,name in enumerate(l2):
        if l1[i] != name:
            return l1[i]
    return l1[-1]

n = int(input())
l1 = []
l2 = []
for i in range(n + n - 1):
    p = input()
    if i < n:
        l1.append(p)
    else:
        l2.append(p)
print(helper(l1,l2))
