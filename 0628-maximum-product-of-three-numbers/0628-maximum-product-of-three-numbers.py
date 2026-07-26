class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n1=nums[-1]*nums[-2]*nums[-3]
        n2=nums[0]*nums[1]*nums[-1]
        return n1 if n1>n2 else n2