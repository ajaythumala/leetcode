class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current_subarray = max_subarray = nums[0]
        for num in nums[1:]:
            current_subarray = max(current_subarray + num, num)
            max_subarray = max(max_subarray, current_subarray)
            
        return max_subarray

#         MAX = SUM = nums[0]
#         for num in nums[1:]:
#             if SUM < 0:
#                 SUM = 0
#             SUM += num
#             MAX = max(MAX, SUM)

#         return MAX
