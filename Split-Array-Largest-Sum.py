class Solution:
    def days_to_finish(self,nums, mid):
        days = 1
        cur = 0
        max_sum = 0
        for i in nums:
            if cur+i > mid:
                days+=1
                cur = 0
            cur += i
            max_sum = max(max_sum, cur)
        return [days, max_sum]


    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums); high = sum(nums)

        while (low < high):
            mid = (low + high)//2
            if self.days_to_finish(nums, mid)[0] > k:
                low = mid + 1 
            else: high = mid
        
        return self.days_to_finish(nums,low)[1]