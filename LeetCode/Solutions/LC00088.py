class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #O((m+n)lg(m+n))
        # nums1[:] = sorted(nums1[:m]+nums2)
        #O(m+n)
        nums3 = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            n1 = nums1[p1] if p1 < m else inf
            n2 = nums2[p2] if p2 < n else inf
            if n1 < n2:
                nums3.append(n1)
                p1 += 1
            else:
                nums3.append(n2)
                p2 += 1
        nums1[:] = nums3