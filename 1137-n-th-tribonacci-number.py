class Solution:
    def tribonacci(self, n: int) -> int:
      # --- Chosen Solution --- # 14-5-22
        if n < 3: 
            return 1 if n else 0
          
        num1, num2, num3 = 0, 1, 1
        
        for _ in range(2, n):
            num1, num2, num3, = num2, num3, num1 + num2 + num3
        return num3
 

# --- Initial Solution --- # 13-5-22
#        if n <= 1:
#             return n
#        elif n == 2:
#             return 1
        
#         num1 = SUM = 0
#         num2 = num3 = 1

# for _ in range(2, n):
#             SUM = num1 + num2 + num3
#             num1 = num2
#             num2 = num3
#             num3 = SUM
#         return SUM
