def feed(count,dog,cat,other,letters):
    try:
        lastdog = count - list(reversed(letters)).index("D")
    except:
        return "YES"
    index = 0
    while index < lastdog:
        if letters[index] == "C":
            cat -= 1
            if cat < 0:
                return "NO"
        elif letters[index] == "D":
            dog -= 1
            cat += other
            
            if dog < 0:
                return "NO"
        index += 1
    return "YES"
t = int(input())
for i in range(t):
    count, dog, cat, other = [int(i) for i in input().split()]
    letters = input()
    print("Case #" + str(i+1)+": "+str(feed(count,dog,cat,other,letters)))
