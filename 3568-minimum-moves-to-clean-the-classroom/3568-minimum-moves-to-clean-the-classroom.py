from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_pos = {}
        start = None
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_pos[(r, c)] = len(litter_pos)
                    
        target_mask = (1 << len(litter_pos)) - 1
        if target_mask == 0: 
            return 0
            
        q = deque([(start[0], start[1], energy, 0, 0)])
        visited = {(start[0], start[1], energy, 0)}
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            r, c, e, mask, steps = q.popleft()
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    nxt_e = e - 1
                    nxt_mask = mask
                    
                    if classroom[nr][nc] == 'L':
                        nxt_mask |= (1 << litter_pos[(nr, nc)])
                        
                    if nxt_mask == target_mask:
                        return steps + 1
                        
                    if classroom[nr][nc] == 'R':
                        nxt_e = energy
                        
                    if nxt_e == 0 and classroom[nr][nc] != 'R':
                        continue
                        
                    if (nr, nc, nxt_e, nxt_mask) not in visited:
                        visited.add((nr, nc, nxt_e, nxt_mask))
                        q.append((nr, nc, nxt_e, nxt_mask, steps + 1))
                        
        return -1