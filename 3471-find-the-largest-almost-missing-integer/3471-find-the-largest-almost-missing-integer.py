class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        return (
            max(nums)  if k==len(nums)  else
            max((k for k,v in Counter(nums).items() if v==1), default = -1)  if k==1   else
            max((k for k,v in Counter(nums).items() if v==1 and k in {nums[0], nums[-1]}), default = -1)
        )
        