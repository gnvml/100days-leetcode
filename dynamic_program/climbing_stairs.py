# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        self.mem = [-1]*n
        if n >= 1:
            self.mem[0] = 1
        if n >=2:
            self.mem[1] = 2
        return self.count(n)
    
    def count(self,n):
        if self.mem[n-1] != -1:
            return self.mem[n-1]
        else:
            self.mem[n-1] = self.count(n-1) + self.count(n-2)
            return self.mem[n-1]
        
        