class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        # ------------- Chosen Approach --------------------- #
        p1 = m - 1
        p2 = n - 1
        
        for p in range(m + n - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >=0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -=1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                
        # ------------- Initial Approach --------------------- #
        
          #shifting an element in order to insert
#         def shift_right_from_index(array, index):
#             i = len(array) - 1
#             while i > index:
#                 array[i] = array[i - 1]
#                 i -= 1
#         i=j=0
#         while i < m and j < n:
#             if nums1[i] < nums2[j]:
#                 i += 1
#             elif nums2[j] < nums1[i]:
#                 shift_right_from_index(nums1, i)
#                 nums1[i] = nums2[j]
#                 j += 1
#                 i += 1
#                 m += 1
#             elif nums1[i] == nums2[j]:
#                 shift_right_from_index(nums1, i)
#                 j += 1
#                 i += 2
#                 m += 1
#         while i < m+n and j < n:
#             nums1[i] = nums2[j]
#             i += 1
#             j += 1
        
    
                
                
                
        
        
