class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
      
# ----- Lesser Time ----- #
      occurs = {}
      result = []
        
      for num in nums1:
            occurs[num] = occurs.get(num , 0) + 1
          
      for num in nums2:
            if num in occurs and occurs[num] > 0 :
                result.append(num)
                occurs[num] -= 1
                
      return result
    
    
# ----- Lesser Space ----- #
#       occurs = {}
#       for num in nums1:
#             occurs[num] = occurs.get(num , 0) + 1
        
#       i = 0
#       for num in nums2:
#             if num in occurs and occurs[num] > 0:
#                 nums1[i] = num
#                 i += 1
#                 occurs[num] -= 1   
                
#         nums1 = nums1[:i]
#         return nums1
      
