class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        if not head or not head.next or not head.next.next:
            return [-1, -1]
            
        min_dist = float('inf')
        first_cp = -1
        prev_cp = -1
        
        prev = head
        curr = head.next
        position = 1
        
        while curr.next:
            nxt = curr.next
            
            is_maxima = curr.val > prev.val and curr.val > nxt.val
            is_minima = curr.val < prev.val and curr.val < nxt.val
            
            if is_maxima or is_minima:
                if first_cp == -1:
                    first_cp = position
                else:
                    min_dist = min(min_dist, position - prev_cp)
                    
                prev_cp = position
                
            prev = curr
            curr = nxt
            position += 1
            
        if first_cp == prev_cp:
            return [-1, -1]
            
        max_dist = prev_cp - first_cp
        
        return [min_dist, max_dist]
