class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        cur_sum = 0
        ans = 0
        for val in nums:
            cur_sum += (val%k)
            ans += mp.get(cur_sum%k, 0)
            mp[cur_sum%k] = mp.get(cur_sum%k,0) + 1

        return ans