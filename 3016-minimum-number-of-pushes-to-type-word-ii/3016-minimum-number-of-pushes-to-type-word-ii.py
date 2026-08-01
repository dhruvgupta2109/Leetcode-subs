class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        counts = sorted(Counter(word).values(), reverse=True)
        ans = 0
        for i, cnt in enumerate(counts):
            ans += cnt * (i // 8 + 1)
        return ans