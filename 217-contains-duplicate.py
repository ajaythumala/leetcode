class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        """
        using comparison with the set object of the given list
        """
        return len(set(nums))!=len(nums)
        
        #----------------------------------------------------#
        """
        using a set
        """
        visited = set() # sets are implemented using hash tables.
        for num in nums: # hence, it is faster to use sets than lists.
            if num in visited:
                return True
            visted.add(num)
        return False
        
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
        
        
             
        
            
        
