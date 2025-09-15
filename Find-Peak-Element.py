class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l,r= 0, n-1
        while(l<r):
            mid = l + (r-l+1)//2
            if nums[mid] < nums[mid-1]:
                r = mid-1
            else:
                l = mid
        return l

        