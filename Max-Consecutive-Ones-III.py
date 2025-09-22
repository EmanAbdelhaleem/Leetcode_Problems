class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        n = len(nums)
        pref = [0]*(n+1)
        ans = 0
        mp = {0:0}
        ans = 0
        for idx, val in enumerate(nums, start = 1):
            pref[idx] = pref[idx-1] + (1-val)
            if pref[idx] <= k:
                ans = idx
            else:
                ans = max(ans, idx - mp.get(pref[idx]-k,idx))
            
            mp[pref[idx]] = min(idx,mp.get(pref[idx],float('inf')))
        return ans

        

            

        