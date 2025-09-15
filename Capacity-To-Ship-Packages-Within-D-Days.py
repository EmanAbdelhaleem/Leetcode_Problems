import math
class Solution:
    def days_to_finish(self,weights, mid):
        days = 1
        cur = 0
        for i in weights:
            if cur+i > mid:
                days+=1
                cur = 0
            cur += i
        return days


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights); high = sum(weights)

        while (low < high):
            mid = (low + high)//2
            if self.days_to_finish(weights, mid) > days:
                low = mid + 1 
            else: high = mid
        
        return low

        