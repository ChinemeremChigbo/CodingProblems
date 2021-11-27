class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        isNegative=(dividend<0)^(divisor<0)
        dividend,divisor=abs(dividend),abs(divisor)
        result=0
        while dividend>=divisor:
            count=0
            while dividend>=divisor<<1<<count:
                count+=1
            result+=1<<count
            dividend-=divisor<<count
        if isNegative:
            result*=-1
        if result>2**31-1:
            result=2**31-1
        elif result<-2**31:
            result=-2**31
        return result    