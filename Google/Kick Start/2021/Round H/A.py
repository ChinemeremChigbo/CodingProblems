def func(s,f):
    goal = set(f)
    total = 0
    closest = {}
    for letter in "abcdefghijklmnopqrstuvwxyz":
        for g in goal:
            lp = ord(letter) - ord("a")
            lg = ord(g) - ord("a")
            dist = min(abs(lg - lp),26 - abs(lg - lp))
            if letter not in closest:
                closest[letter] = dist
            else:
                closest[letter] = min(closest[letter],dist)
    for l in s:
        total += closest[l]
    return total
t = int(input())
for i in range(t):
    s = input()
    f = input()
    print("Case #" + str(i+1)+": "+str(func(s,f)))
