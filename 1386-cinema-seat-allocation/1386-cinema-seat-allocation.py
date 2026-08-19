class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        reservedSeats.sort()
        i = 0
        cnt = 0
        for row in range(1, n+1):
            if i == len(reservedSeats): 
                cnt += 2 * (n - row + 1)
                break
            elif reservedSeats[i][0] > row:
                cnt += 2
            else:
                g1 = g2 = g3 = True
                while i < len(reservedSeats) and reservedSeats[i][0] == row:
                    seat = reservedSeats[i][1]
                    i += 1
                    if 2 <= seat <= 5: g1 = False
                    if 4 <= seat <= 7: g2 = False
                    if 6 <= seat <= 9: g3 = False
                if g1 and g3:
                    cnt += 2
                elif g1 or g2 or g3:
                    cnt += 1
        return cnt
            