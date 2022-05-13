class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        first = 0
        last = n - 1
        
        for i in range(n-1, -1, -1):
            left = abs(nums[first])
            right = abs(nums[last])
            
            if left < right:
                square = right
                last -= 1
            else:
                square = left
                first += 1
            result[i] = square * square
        return result
    
        
        
        
        # Note: shifting array elements is an expensive operation
#         def shift_left_from_index(array, index):
#             i = 0
#             while i < index:
#                 array[i] = array[i + 1]
#                 i += 1
        
#         p = len(nums) - 1
        
#         while p >= 0:
#             first = nums[0]
#             last = nums[p]
#             if p == 0:
#                 nums[p] == first * first
                
#             if abs(last) >= abs(first):
#                 nums[p] = last * last
#                 p -= 1
#             elif abs(first) > abs(last):
#                 shift_left_from_index(nums, p)
#                 nums[p] = first * first
#                 p -= 1
#         return nums
                
            
                
            
                
                
