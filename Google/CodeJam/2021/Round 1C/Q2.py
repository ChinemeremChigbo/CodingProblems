
def func(b,fin):
    sq1 = sum(i*i for i in fin)
    sq2 = sum(i for i in fin)
    lo = -pow(10,18)
    hi = pow(10,18)
    count = 0
    while count < 100000:
        mid = (lo+hi)//2
        r1 = sq1 + mid*mid
        r2 = (sq2 + mid) * (sq2 + mid)
        if r1 < r2:
            hi =  mid
        elif r1 == r2:
            return str(mid)
        else:
            lo = mid + 1
        count += 1
    return "IMPOSSIBLE"

t = int(input())
for i in range(t):
    a,b = input().split()
    fin = list(map(int, input().split()))
    print("Case #" + str(i+1)+": "+str(func(int(b),fin)))