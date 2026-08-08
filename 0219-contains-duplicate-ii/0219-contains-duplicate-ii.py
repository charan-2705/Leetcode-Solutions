class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        n=len(nums)
        myset=set()
        for i in range(n):
            if nums[i] in myset:
                return True
            myset.add(nums[i])
            if i>=k:
                myset.remove(nums[i-k])
        return False