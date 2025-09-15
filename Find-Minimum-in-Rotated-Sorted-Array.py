class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l , r = 0, n-1

        # if not rotated, one element
        if nums[r] >= nums[l]: return nums[0]

        while(l <= r):
            mid = l + (r-l)//2

            if mid > 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] >= nums[0]:
                l = mid+1
            else:
                r = mid - 1

        return nums[l]