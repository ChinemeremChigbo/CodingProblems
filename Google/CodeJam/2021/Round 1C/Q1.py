from itertools import permutations
def func(r):
    print(r)
    def check(word):
        seen = set()
        res = ""
        for letter in word:
            if letter not in seen:
                seen.add(letter)
                res += letter
            else:
                if letter != res[-1]:
                    return False
        if len(res) == 1:
            return (res,"",res,seen)
        elif len(res) == 2:
            return (res[0], "", res[1],seen)
        else:
            return (res[0], res[1:-1] ,res[-1],seen)

    final = []
    count = 0
    while r and count < 50:
        next = r.pop()
        newr = []
        print(r)
        for word in r:
            print(word,next,final)
            if word[-1] == next[0]:
                next = word + next
            elif word[0] == next[-1]:
                next = next + word
            else: newr.append(word)
        r = newr
        # print(r)
        final.append(next)
        count += 1
    print(final)
    return ""



t = int(input())
for i in range(t):
    s = int(input())
    r = input().split()
    print("Case #" + str(i+1)+": "+func(r))
