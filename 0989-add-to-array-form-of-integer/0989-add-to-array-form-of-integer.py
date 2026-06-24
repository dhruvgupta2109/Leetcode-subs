class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        st=""
        for i in num:
            st+=str(i)
        n=int(st)+k
        l=[]
        s=str(n)
        for i in s:
            l.append(int(i))
        return l
