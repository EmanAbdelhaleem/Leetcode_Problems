class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # encode arr[r][c] = arr[r*max_c + c]
        # decode r = x//max_c, c = x%c

        lo , hi = 0, len(matrix)*len(matrix[0]) - 1
        n_c = len(matrix[0])
        while(lo<=hi):
            mid = lo + (hi-lo)//2
            r = mid // n_c
            c = mid % n_c
            if(matrix[r][c] == target):
                return True
            elif matrix[r][c] < target:
                lo = mid+1
            else:
                hi = mid-1
        return False
        