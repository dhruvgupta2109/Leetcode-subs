class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        s=[]
        l=[]
        curr=[]
        while len(s)!=len(nums):
            for i in nums:
                if len(curr)==0:
                    curr.append(i)
                    s.append(i)
                else:
                    x=curr[-1]
                    if x+1==i:
                        curr.append(i)
                        s.append(i)
                    else:
                        if len(curr)==1:
                            l.append(str(curr[0]))
                            curr=[i]
                            s.append(i)
                        else:
                            st=str(str(curr[0])+"->"+str(curr[-1]))
                            l.append(st)
                            curr=[i]
                            s.append(i)
        if len(curr)==1:
            l.append(str(curr[0]))
        elif len(curr)>1:
            st=str(str(curr[0])+"->"+str(curr[-1]))
            l.append(st)
        return l

                