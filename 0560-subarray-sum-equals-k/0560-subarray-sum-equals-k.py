class Solution(object):
    def subarraySum(self, nums, k):
        csum=0;count=0;prefixsum={};n=len(nums)
        for i in range(n):
            csum+=nums[i]
            if csum==k:
                count+=1
            if csum-k in prefixsum:
                count+=prefixsum[csum-k]
            prefixsum[csum]=prefixsum.get(csum,0)+1
        return count