class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tx = 0
        nz = False
        
        for num in nums:
            tx ^= num
            if num != 0:
                nz = True
                
        if tx != 0:
            return len(nums)
        if nz:
            return len(nums) - 1
        return 0
