class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        shift = n + 1
        bit = [0] * (2 * n + 2)
        
        def update(idx, val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        update(shift, 1)
        current_sum = 0
        total_subarrays = 0
        
        for num in nums:
            if num == target:
                current_sum += 1
            else:
                current_sum -= 1
            total_subarrays += query(current_sum + shift - 1)
            update(current_sum + shift, 1)
            
        return total_subarrays