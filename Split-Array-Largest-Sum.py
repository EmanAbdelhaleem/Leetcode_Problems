class Solution:
    def splits_when_lar_sum(self,nums, lar_sum):
        splits = 1
        cur = 0
        for i in nums:
            if cur+i > lar_sum:
                splits+=1
                cur = 0
            cur += i
        return splits


    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums); high = sum(nums)

        while (low < high):
            mid = (low + high)//2
            if self.splits_when_lar_sum(nums, mid) > k:
                low = mid + 1 
            else: high = mid
        
        return low