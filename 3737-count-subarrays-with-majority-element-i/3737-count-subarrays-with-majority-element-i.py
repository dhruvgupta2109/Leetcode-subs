class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        c= 0
        for s in range(n):
            tc = 0
            for e in range(s, n):
                if nums[e] == target:
                    tc += 1
                if tc > (e - s + 1) / 2:
                    c += 1
        return c