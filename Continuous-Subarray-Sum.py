class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        mp = {0:-1}
        cur_sum = 0
        for idx,val in enumerate(nums):
            cur_sum += (val%k)
            l = mp.get(cur_sum%k, -2)
            if l != -2 and idx-l >=2:
                return True
            mp[cur_sum%k] = min(idx, mp.get(cur_sum%k,float('inf')))

        return False
        