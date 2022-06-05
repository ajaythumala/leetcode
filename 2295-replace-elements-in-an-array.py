class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        op_map = {}
        op_len = len(operations) - 1
        
        for i in range(op_len, -1, -1):
            op_map[operations[i][0]] = op_map.get(operations[i][1], operations[i][1])

        for i in range(len(nums)):
            if nums[i] in op_map:
                nums[i] = op_map[nums[i]]
        return nums

            
