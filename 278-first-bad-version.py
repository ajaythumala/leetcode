# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        (left, right) = (1, n)
        
        while left <= right:
            pivot = left + ((right - left) // 2)
            
            if isBadVersion(pivot) == True:
                if isBadVersion(pivot - 1) == False or (pivot - 1) < 0:
                    return pivot
                else:
                    right = pivot - 1
                    
            else:
                left = pivot + 1
        
        
