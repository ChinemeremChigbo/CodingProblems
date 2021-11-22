class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1+nums2
        nums3.sort()
        length = len(nums3)
        if length%2 == 0:
            return (nums3[int(length/2)-1]+nums3[int(length/2)])/2        
        else:
            return nums3[int(length/2)]