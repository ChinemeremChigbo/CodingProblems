
def func(r, c):
    res = []
    for i in range((r*2)+1):
        res.append([])
        for j in range(c):
            if i % 2 == 0:
                if i == 0 and j == 0:
                    res[-1] += ".."
                else:
                    res[-1] += "+-"
            else:
                if i == 1 and j == 0:
                    res[-1] += ".."
                else:
                    res[-1] += "|."
        else:
            if i % 2 == 0:
                res[-1] += "+"
            else:
                res[-1] += "|"
    for row in res:
        print("".join(row))

    return


t = int(input())
for i in range(t):
    r, c = map(int, input().split())
    print("Case #" + str(i+1)+":")
    func(r, c)
