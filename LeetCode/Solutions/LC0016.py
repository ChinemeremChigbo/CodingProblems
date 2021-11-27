class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestNum = 1000
        nums.sort()
        for i in range(len(nums)):
            pointer1 = 0
            pointer2 = len(nums)-1
            for j in range(len(nums)-1):
                if (pointer1 == i):
                    pointer1 += 1
                    continue
                if (pointer2 == i):
                    pointer2 -= 1
                    continue
                else:
                    if nums[i]+nums[pointer1]+nums[pointer2]>target:
                        if (-(target-(nums[i]+nums[pointer1]+nums[pointer2]))) < abs(target - closestNum):
                            closestNum = nums[i]+nums[pointer1]+nums[pointer2]
                        pointer2 -= 1
                    elif nums[i]+nums[pointer1]+nums[pointer2]<target:
                        if ((target-(nums[i]+nums[pointer1]+nums[pointer2]))) < abs(target - closestNum):
                            closestNum = nums[i]+nums[pointer1]+nums[pointer2]
                        pointer1 +=1
                    else:
                        return nums[i]+nums[pointer1]+nums[pointer2]
        return(closestNum)