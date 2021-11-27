class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        nums = sorted(nums)
        numList = []
        uniqueDict = {}
        pointerLeft = 0
        pointerRight = len(nums)-1
        for b in range(len(nums)):
            for a in range(len(nums)):
                for i in range(len(nums)-2):
                    if pointerLeft == a:
                        continue
                    elif pointerRight == a:
                        continue
                    else:
                        if pointerRight - pointerLeft == 1:
                            pointerLeft = 0
                            pointerRight = len(nums)-1
                            break
                        elif nums[a]+nums[pointerLeft]+nums[pointerRight]+nums[b]==target and a!=b and a!=pointerLeft and a!=pointerRight and pointerLeft!=pointerRight and pointerLeft!=b and pointerRight!=b:
                            if str([sorted([nums[a],nums[pointerLeft],nums[pointerRight],nums[b]])]) not in uniqueDict:
                                uniqueDict[str([sorted([nums[a],nums[pointerLeft],nums[pointerRight],nums[b]])])] = None
                                numList += [sorted([nums[a],nums[pointerLeft],nums[pointerRight],nums[b]])]
                            pointerLeft +=1
                        elif nums[a]+nums[pointerLeft]+nums[pointerRight]+nums[b]<target:
                            pointerLeft +=1
                        else:
                            pointerRight -=1
                pointerLeft = 0
                pointerRight = len(nums)-1
        return(numList)
