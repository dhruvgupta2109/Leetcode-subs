class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        c=0
        for i in patterns:
            if i in word:
                c+=1
        return c