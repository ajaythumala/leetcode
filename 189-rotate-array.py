class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # --- O(n) time complexity --- #
        n = len(nums)
        
        array = [0] * n
        
        for i in range(n):
            array[(i + k) % n] = nums[i]
            
        nums[:] = array
        
        
        # --- O(n * k) time complexity--- #
#         for _ in range(k):
#             last = nums[n - 1]            
#             for pos in range(n - 1, -1, -1):
#                 nums[pos] = nums[pos - 1]
#             nums[0] = last
                
