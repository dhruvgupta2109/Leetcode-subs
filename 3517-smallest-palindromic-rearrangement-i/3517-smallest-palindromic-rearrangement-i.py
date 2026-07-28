class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n==1:
            return s
        x=sorted(s[:n/2])
        ans=""
        for i in x:
            ans+=i
        if n%2==0:
            ans+=ans[::-1]
            return ans
        c=ans
        ans+=s[(n//2)]
        ans+=c[::-1]
        return ans
