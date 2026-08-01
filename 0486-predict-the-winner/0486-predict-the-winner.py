class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = {}
        def best_diff(i, j):
            if i == j: return nums[i]
            if (i, j) not in memo:
                memo[(i, j)] = max(nums[i] - best_diff(i + 1, j), nums[j] - best_diff(i, j - 1))
            return memo[(i, j)]
            
        s1 = 0
        s2 = 0
        t = 1
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if t == 1:
                if l != r:
                    m = l if nums[l] - best_diff(l + 1, r) >= nums[r] - best_diff(l, r - 1) else r
                    s1 += nums[m]
                    if m == l: l += 1
                    else: r -= 1
                    t = 2
                else:
                    s1 += nums[l]
                    l += 1
            else:
                if l != r:
                    m = l if nums[l] - best_diff(l + 1, r) >= nums[r] - best_diff(l, r - 1) else r
                    s2 += nums[m]
                    if m == l: l += 1
                    else: r -= 1
                    t = 1
                else:
                    s2 += nums[l]
                    l += 1
                    
        return s1 >= s2
