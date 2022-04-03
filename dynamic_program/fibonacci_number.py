# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:
        self.mem = [-1]*(n + 1)
        self.mem[0] = 0
        if n >= 1:
            self.mem[1] = 1
            
        return self.fib_sub(n)
    
    def fib_sub(self, n):
        if self.mem[n] != -1:
            return self.mem[n]
        else:
            self.mem[n] = self.fib_sub(n-1) + self.fib_sub(n-2)
            return self.mem[n]
