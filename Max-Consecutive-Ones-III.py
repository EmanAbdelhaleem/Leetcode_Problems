class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        n = len(nums)
        flipped = 0
        sum = 0
        ans = 0
        while (l < n):
            while r < n:
                if (flipped == k and nums[r] == 0): break
                sum += 1
                flipped += (1-nums[r])
                r+=1
            
            ans = max(ans,sum)

            sum -= 1
            flipped -= (1-nums[l])
            l+=1
        
        return ans

        