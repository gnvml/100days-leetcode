# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Using binary search, nlog(n)
        '''
        
        self.nums = nums.copy()
        self.nums.sort()
        two_values = []
        for i in range(len(self.nums)):
            sub_target = target - self.nums[i]
            left = i + 1
            right = len(self.nums) -1
            index =  self.search(sub_target, left, right)
            if index != -1:
                two_values = [self.nums[i], self.nums[index]]
                break
        result = []
        for i in range(len(nums)):
            if nums[i] in two_values:
                two_values.remove(nums[i])
                result.append(i)
        return result
        
    def search(self, sub_target, left, right):
        if right == left:
            if self.nums[left] == sub_target:
                return left
            else:
                return -1
        mid_id = left + (right - left)//2
        if self.nums[mid_id] < sub_target:
            left = mid_id + 1
            return self.search(sub_target, left, right)
        else:
            right = mid_id
            return self.search(sub_target, left, right)