def func(s,f):
    count = 0
    dicti = [None,None,None]
    while f not in dicti:
        dicti[count%3] = f
        f = f.replace("01","2").replace("12","3").replace("23","4").replace("34","5").replace("45","6").replace("56","7").replace("67","8").replace("78","9").replace("89","0").replace("90","1")
        count += 1
    return f

t = int(input())
for i in range(t):
    s = input()
    f = input()
    print("Case #" + str(i+1)+": "+str(func(s,f)))