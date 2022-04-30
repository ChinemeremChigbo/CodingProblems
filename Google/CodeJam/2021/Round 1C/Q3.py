def func(fin):
    fin.sort(reverse=True)
    maxL = 0
    l = 0
    n = len(fin)
    for i in range(n):
        if fin[-1] > l:
            l += 1
        fin.pop()
        maxL = max(maxL, l)
    return maxL


t = int(input())
for i in range(t):
    input()
    print("Case #" + str(i+1)+": "+str(func(list(map(int, input().split())))))
