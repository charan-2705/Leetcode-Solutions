class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            a = min(nums)
            for i in range(len(nums)):
                if nums[i]==a:
                    nums[i]*=multiplier
                    break
        return nums
        