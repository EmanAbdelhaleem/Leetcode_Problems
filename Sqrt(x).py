class Solution:
    def mySqrt(self, x: int) -> int:
        def check(x):
            return x*x
        l = 0; r = x

        while(l < r):
            mid = l + (r-l+1)//2

            if check(mid) == x:
                return mid
            elif check(mid) < x:
                l = mid 
            else:
                r = mid - 1
        
        return l
            

        