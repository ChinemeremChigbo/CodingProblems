# def evaluate(n,string):
#     oneList = []
#     for i,num in enumerate(string):
#         if num == "1":
#             oneList.append(i)
#             string[i] = 0
#     count = 0
#     while oneList:
#         newList = []
#         count += 1
#         for el in oneList:
#             if el - 1 > -1 and string[el-1] == "0":
#                 newList.append(el-1)
#             if el + 1 < n and string[el+1] == "0":
#                 newList.append(el+1)
#         oneList = newList
#         for le in oneList:
#             string[le] = count
#     return sum(string)
# t = int(input())
# for i in range(t):
#     n = int(input())
#     q = list(input())
#     print("Case #",end="")
#     print(str(i+1)+": "+str(evaluate(n,q)))