class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}
        for index in range(len(nums)):
            dictionary[nums[index]] = dictionary.get(nums[index], index)
            if target-nums[index] in dictionary and (index != dictionary[target-nums[index]]):
                return dictionary[target-nums[index]], index
        
        
