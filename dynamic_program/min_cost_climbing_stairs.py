# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.n = len(cost)
        self.mem = [-1]*(self.n)
        
        # Cause n >=2
        self.cost = cost
        self.mem[0] = cost[-1]
        self.mem[1] = min(cost[-1] + cost[-2], cost[-2])
        '''
        2 cases:
        1. p(0) + p(n-1), p(0) + p(n-2)
        2. p(1) + p(n-2), p(1) + p(n-3)
        
        p(n) = min(v(length - n) + p(n-1), v(length - n) + p(n-2))
        '''
        return min([cost[0] + self.min_cost(self.n-1), \
                    cost[0] + self.min_cost(self.n-2), \
                    cost[1] + self.min_cost(self.n-2), \
                    cost[1] + self.min_cost(self.n-3)])
    
    def min_cost(self, n):
        if n == 0:
            return 0
        if self.mem[n-1] != -1:
            return self.mem[n-1]
        else:
            self.mem[n-1] = min(self.cost[self.n-n] + self.min_cost(n-1),\
                               self.cost[self.n-n] + self.min_cost(n-2))
            return self.mem[n-1]