class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=str(n)
        f=0
        if "9" in s:
            s=s.replace("9","",1)
            f=9
            if "9" in s:
                return 81
        elif "8" in s:
            s=s.replace("8","",1)
            f=8
            if "8" in s:
                return 64
        elif "7" in s:
            s=s.replace("7","",1)
            f=7
            if "7" in s:
                return 49
        elif "6" in s:
            s=s.replace("6","",1)
            f=6
            if "6" in s:
                return 36
        elif "5" in s:
            s=s.replace("5","",1)
            f=5
            if "5" in s:
                return 25
        elif "4" in s:
            s=s.replace("4","",1)
            f=4
            if "4" in s:
                return 16
        elif "3" in s:
            s=s.replace("3","",1)
            f=3
            if "3" in s:
                return 9
        elif "2" in s:
            s=s.replace("2","",1)
            f=2
            if "2" in s:
                return 4
        elif "1" in s:
            s=s.replace("1","",1)
            f=1
            if "1" in s:
                return 1
        if f==0:
            return 0
        if "9" in s:
                return 9*f
        if "8" in s:
                return 8*f
        if "7" in s:
                return 7*f
        if "6" in s:
                return 6*f
        if "5" in s:
                return 5*f
        if "4" in s:
                return 4*f
        if "3" in s:
                return 3*f
        if "2" in s:
                return 2*f
        if "1" in s:
                return 1*f
        return 0