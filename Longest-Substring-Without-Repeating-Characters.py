class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        ans = 0
        mp = {}
    
        while(r < len(s)):
            if(s[r] in mp):
                l = max(mp[s[r]]+1,l)
                
            mp[s[r]] = r
            ans = max(ans,r-l+1)
            r+=1
            
           
        return ans

        