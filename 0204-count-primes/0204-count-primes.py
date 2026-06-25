class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1 or n==2:
            return 0
        d=[1]*n
        d[0]=d[1]=0
        for i in range (2,int(n**0.5) + 1):
            if d[i]==1:
                for j in range(i*i, n, i):
                    d[j]=0
        return sum(d)
