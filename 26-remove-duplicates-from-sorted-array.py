class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        next_unique = 1
        while unique < len(nums) and next_unique < len(nums):
            if nums[unique] != nums[next_unique]:
                unique += 1
                nums[unique] = nums[next_unique]
                next_unique += 1
            else:
                next_unique += 1
        return unique + 1
