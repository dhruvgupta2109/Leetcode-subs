class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        ans=1
        if 1 in d:
            if d[1]%2==1:
                ans=max(ans,d[1])
            else:
                ans=max(ans,d[1]-1)
        for x in d:
            if x==1:
                continue
            cur=x
            c=0
            while cur in d and d[cur]>=2:
                c+=2
                cur=cur*cur
            if cur in d:
                ans=max(ans,c+1)
            else:
                ans=max(ans,c-1)
        return ans