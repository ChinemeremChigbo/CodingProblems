# def dfs(total,cap,trees):
#     mem = {}
#     def explore(comb,cap,count):
#         if comb > cap:
#             return -1
#         if comb == cap:
#             return count
#         mem[comb] = explore()

#         if mem[cap]: return mem[cap]
#         else: return -1

        

#     return explore()

#     return -1
# t = int(input())
# for i in range(t):
#     total, cap = [int(i) for i in input().split()]
#     trees = [int(i) for i in input().split()]
#     print("Case #" + str(i+1)+": "+str(dfs(total,cap,trees)))
def bfs(total,cap,trees):
    bfsList = {(0,-1,0)}
    # bfsDict = {}
    count = 0

    while bfsList:
        newList = set()
        for comb,index,skips in bfsList:
            if comb == cap: return count
            for num in range(index + 1, total):
                if comb + trees[num] <= cap:
                    if index == -1:
                        newList.add((comb + trees[num], num, 0))
                    else:
                        if num == index + 1 and skips == 0:
                            newList.add((comb + trees[num], num, 0))
                        elif num == index + 1 and skips == 1:
                            newList.add((comb + trees[num], num, 1))
                        elif skips == 0:
                            newList.add((comb + trees[num], num, 1))
        bfsList = newList
        count += 1

    return -1
t = int(input())
for i in range(t):
    total, cap = [int(i) for i in input().split()]
    trees = [int(i) for i in input().split()]
    print("Case #" + str(i+1)+": "+str(bfs(total,cap,trees)))