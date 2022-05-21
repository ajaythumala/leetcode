# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        (left, right) = (1, n)
        while left < right:
            pivot = (left + right) // 2 # could overflow in other languages : use pivot = left + ((right - left) // 2) if needed
            if isBadVersion(pivot):
                right = pivot
            else:
                left = pivot + 1
        return left #left, not pivot as it fails in the case of there being only 1 element.
                    #we assume this because there is always one bad version in the input.
                    #verified as the submission was accepted.
              
#         while left <= right:
#             pivot = (left + right) // 2
#             if isBadVersion(pivot) == True:
#                 if isBadVersion(pivot - 1) == False or (pivot - 1) < 0:
#                     return pivot
#                 else:
#                     right = pivot - 1

        
        
