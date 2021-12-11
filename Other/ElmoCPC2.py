from collections import defaultdict
def helper(n,k,l):
    ls = sorted(l)
    lDict = defaultdict(set)
    a = 1
    for i,num in enumerate(ls):
        if i and i%k == 0:
            a += 1
        lDict[a].add(num)
    a = 1
    pointer = 0
    popped = 0
    res = 0
    while popped < n - k:
        stop = True
        if popped and popped%k == 0:
            a += 1
        if l[pointer] in lDict[a]:
            if pointer != 0:
                res += 1
            l.pop(pointer)
            popped += 1
            pointer -= 1
            stop = False
        pointer += 1
        if pointer == len(l):
            if stop:
                break
            else:
                pointer = 0
    return res
    


n, k = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]
print(helper(n,k,l))