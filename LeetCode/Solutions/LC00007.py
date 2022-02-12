class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x<0:
            x = -x
            strInt = str(x)[::-1]
            if -int(strInt) < -2147483648:
                return(0)
            else:
                return(-(int(strInt)))
        else:
            strInt = str(x)[::-1]
            if int(strInt) > 2147483647:
                return(0)
            else:
                return(int(strInt))