# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float(-inf)
        current_max = float(-inf)
        for val in nums:
            current_max = max(val, val + current_max)
            max_sum = max(max_sum,current_max)
        return max_sum