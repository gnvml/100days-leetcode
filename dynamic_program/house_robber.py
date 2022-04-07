# https://leetcode.com/problems/house-robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        f(i): max value to start from house i
        f(0) = max(v[0] + f(2), f(1))
        -> f(i) = max(v[i] + f(i + 2) , f(i+1))
        f(n-1) = v[n-1]
        f(n-2) = max(v[n-1], v[n-2])
        '''
        self.nums = nums
        n = len(nums)
        self.mem = [-1]*(n)
        if n >= 1:
            self.mem[-1] = nums[-1]

        if n >= 2:
            self.mem[-2] = max(nums[-1], nums[-2])
        
        if n == 1:
            return self.mem[-1]
        if n == 2:
            return self.mem[-2]
        
        return max(nums[0] + self.sub_rob(2), self.sub_rob(1))
    
    def sub_rob(self, i):
        if self.mem[i] != -1:
            return self.mem[i]
        else:
            self.mem[i] = max(self.nums[i] + self.sub_rob(i+2), self.sub_rob(i+1))
            return self.mem[i]