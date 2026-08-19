class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            s=str(n)
            m=1
            for i in s:
                m*=int(i)
            if m%t==0:
                return n
            n+=1