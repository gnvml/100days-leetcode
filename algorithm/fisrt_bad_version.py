# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# https://leetcode.com/problems/first-bad-version/
class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n ==1 :
            return n
        return self.sub_search( 1, n)
    
    def sub_search(self, left, right):
        if right-left == 1:
            if isBadVersion(left) and isBadVersion(right):
                return left
            if isBadVersion(right):
                return right

        mid_id = left + (right - left)//2
        if not isBadVersion(mid_id):
            left = mid_id
            return self.sub_search(left, right)
        else:
            right = mid_id
            return self.sub_search(left, right)