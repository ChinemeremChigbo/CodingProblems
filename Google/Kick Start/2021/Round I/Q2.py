
def func(fin):
    c = min(fin[0][0], fin[1][0], fin[2][0])
    m = min(fin[0][1], fin[1][1], fin[2][1])
    y = min(fin[0][2], fin[1][2], fin[2][2])
    k = min(fin[0][3], fin[1][3], fin[2][3])
    if c + m + y + k >= 1000000:
        c1 = min(c, 1000000 - 3)
        m1 = min(m, 1000000 -  c1 - 2)
        y1 = min(y, 1000000 -  c1 - m1 - 1)
        k1 = min(k, 1000000 - c1 - m1 - y1)
        return " ".join(map(str,[c1, m1, y1, k1]))
    else:
        return("IMPOSSIBLE")


t = int(input())
for i in range(t):
    fin = []
    for j in range(3):
        c, m, y, k = map(int, input().split())
        fin.append((c, m, y, k))
    print("Case #" + str(i+1)+": "+str(func(fin)))
