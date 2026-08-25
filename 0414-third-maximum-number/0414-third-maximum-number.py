class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = set(nums)
        res = list(l)
        res.sort()
        if len(res)>2:
            return res[-3]
        return max(res)
        