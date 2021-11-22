
def bfs(total,cap,trees):
    bfsList = [(0,-1,0)]
    count = 0

    while bfsList:
        newList = []
        for comb,index,skips in bfsList:
            if comb == cap: return count
            for num in range(index + 1, total):
                if comb + trees[num] <= cap:
                    if num == index + 1:
                        newList.append((comb + trees[num], num, 0))
                    elif skips == 0:
                        newList.append((comb + trees[num], num, 1))
        bfsList = newList
        count += 1

    return -1
t = int(input())
for i in range(t):
    total, cap = [int(i) for i in input().split()]
    trees = [int(i) for i in input().split()]
    print("Case #" + str(i+1)+": "+str(bfs(total,cap,trees)))