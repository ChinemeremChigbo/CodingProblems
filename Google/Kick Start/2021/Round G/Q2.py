def water(furn):
    print("wooo",furn)
    def distance(originx,originy,BLX,BLY,TRX,TRY):
        if originx < BLX:
            if originy < BLY: #bottom left
                return  (BLX - originx) + (BLY - originy)
            elif originy > TRY: #top left
                return (BLX - originx) + (originy - BLY)
            else: # left 
                 return BLX - originx
        elif originx > TRX:
            if originy < BLY: #bottom right
               return  (originx - BLX) + (BLY - originy)
            elif originy > TRY: #top right
                 return (originx - BLX) + (originy - BLY)
            else: # right
                 return  originx - BLX
        elif originy < BLY: #bottom
            return BLY - originy
        elif originy > BLY: #top
            return  originy - BLY
        else: #inside 
            return 0
t = int(input())
for i in range(t):
    objects = int(input())
    furn = []
    for j in range(objects):
        a,b,c,d = [int(i) for i in input().split()]
        furn.append((a,b,c,d))
    print("Case #" + str(i+1)+": "+str(water(furn)))
