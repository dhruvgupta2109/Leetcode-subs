class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        ans = 0
        l = 0
        
        for r, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1
            while freq[num] > k:
                freq[nums[l]] -= 1
                l += 1
            if r - l + 1 > ans:
                ans = r - l + 1
                
        return ans