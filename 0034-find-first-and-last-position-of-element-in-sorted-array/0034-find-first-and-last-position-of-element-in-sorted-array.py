
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        if nums and nums[0] <= target <= nums[~0]:
            
            lft, rgt = bisect_left(nums, target), bisect_right(nums, target)
            if lft < rgt: return [lft, rgt - 1]

        return [-1,-1]