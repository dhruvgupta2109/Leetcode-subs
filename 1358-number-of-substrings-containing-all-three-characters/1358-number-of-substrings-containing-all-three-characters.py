class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        f=0
        for e in range(len(s)):
            while ("a" in s[f:e+1]) and ("b" in s[f:e+1]) and ("c" in s[f:e+1]):
                c+=(len(s)-e)
                f+=1
        return c