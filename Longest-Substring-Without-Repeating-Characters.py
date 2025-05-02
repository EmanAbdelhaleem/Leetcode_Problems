class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        ans = 0
    
        while(r < len(s)):
            temp = s[l:r+1]
            while(l <=r and len(temp) != len(set(temp))): 
                l+=1
                temp = s[l:r+1]
            ans = max(ans,r-l+1)
            r+=1
            
           
        return ans

        