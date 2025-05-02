class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        ans = 0
        temp = set()
    
        while(r < len(s)):
            while(l <=r and (s[r] in temp)): 
                temp.remove(s[l])
                l+=1
                
            temp.add(s[r])
            ans = max(ans,r-l+1)
            r+=1
            
           
        return ans

        