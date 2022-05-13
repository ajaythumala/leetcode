class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        num1 = SUM = 0
        num2 = 1
        for i in range(2, n + 1):
            SUM = num1 + num2
            num1 = num2
            num2 = SUM
        return SUM
            
        
