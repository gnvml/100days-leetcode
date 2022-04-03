class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        #Solution 1 nlog(n)
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False
        '''
        #Solution 2: O(n)
        out_dict = {}
        for num in nums:
            if num in out_dict:
                return True
            else:
                out_dict[num] = 1
        return False
            