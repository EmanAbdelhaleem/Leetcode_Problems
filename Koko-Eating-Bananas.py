import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(piles, mid):
            needed_h = 0
            for i in piles:
                needed_h += (i + mid -1)//mid
            return needed_h
            
        
        lo, hi =  1, sum(piles)
        while ( lo < hi): 
            mid = lo + (hi-lo)//2
            if check(piles, mid) > h:
                lo = mid+1
            else:
                hi = mid
        return lo