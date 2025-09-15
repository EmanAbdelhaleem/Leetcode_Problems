import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        first = bisect.bisect_left(nums, target)
        last = bisect.bisect_right(nums,target) - 1

         
        if first == len(nums) or nums[first] != target:
            return [-1,-1]
        else: return [first, last]