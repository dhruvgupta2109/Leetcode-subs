import itertools
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[0]
        for i in range(n):
            for j in range(len(l)-1,-1,-1):
                l.append(l[j]+(1<<i))
        return l