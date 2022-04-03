class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.sub_search(nums, target, 0, len(nums))
    
    def sub_search(self, nums, target, left, right):    
        if right-left == 1:
            if nums[left] == target:
                return left
            else:
                return -1
        mid_id = left + len(nums[left:right])//2
        mid_val = nums[mid_id]
        if mid_val <= target:
            left = mid_id
            return self.sub_search(nums, target, left, right)
        else:
            right = mid_id
            return self.sub_search(nums, target, left, right)