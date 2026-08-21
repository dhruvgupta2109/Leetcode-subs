class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
            
        suspicious = set()
        q = [k]
        suspicious.add(k)
        
        while q:
            curr = q.pop(0)
            for nxt in adj[curr]:
                if nxt not in suspicious:
                    suspicious.add(nxt)
                    q.append(nxt)
                    
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))
                
        return [i for i in range(n) if i not in suspicious]
