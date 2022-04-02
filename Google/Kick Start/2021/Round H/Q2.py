def func(s,f):
    R = "".join(["1" if i in "ROPA" else "0" for i in f])
    Y = "".join(["1" if i in "YOGA" else "0" for i in f])
    B = "".join(["1" if i in "BPGA" else "0" for i in f])
    def cont(arr):
        res = arr.count("10")
        return res if arr[-1] == "0" else res + 1
    return sum([cont(R),cont(Y),cont(B)])
t = int(input())
for i in range(t):
    s = input()
    f = input()
    print("Case #" + str(i+1)+": "+str(func(s,f)))