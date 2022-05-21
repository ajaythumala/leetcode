class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}
        for index in range(len(nums)):
            dictionary[nums[index]] = dictionary.get(nums[index], index)
            if target-nums[index] in dictionary and (index != dictionary[target-nums[index]]):
                return dictionary[target-nums[index]], index
        
        
        #alternate method: 22.05.22 - using enumerate function
        occurs = {}
        for index, num in enumerate(nums):
            occurs[num] = occurs.get(num, index)
            if target - num in occurs and index != occurs[target - num]:
                return occurs[target - num], index
        
