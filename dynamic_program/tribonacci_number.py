# https://leetcode.com/problems/n-th-tribonacci-number/submissions/
class Solution:
    def tribonacci(self, n: int) -> int:
        self.mem = [-1]*(n+1)
        if n >= 0:
            self.mem[0] = 0
        if n >= 1:
            self.mem[1] = 1
        if n >= 2:
            self.mem[2] = 1
        if n >= 3:
            self.mem[3] = 2
        return self.sub_tri(n)
    
    def sub_tri(self, n):
        if n == 0 or n == 1 or n ==2 or n ==3:
            return self.mem[n]
        if self.mem[n] != -1:
            return self.mem[n]
        else:
            return 2*self.sub_tri(n-1) - self.sub_tri(n-4)
            
            