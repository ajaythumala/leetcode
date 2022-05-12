class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        """
        using comparison with the set object of the given list
        """
        return len(set(nums))!=len(nums)
        
        #----------------------------------------------------#
        
        """
        using dictionary
        """
        histogram = {}
        
        for num in nums:
            histogram[num] = histogram.get(num, 0) + 1
            
        for i in histogram.values():
            if i > 1:
                return True
        return False
        
        
             
        
            
        
