class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c1 = nums.count(0)
        c2 = nums.count(1)
        c3 = nums.count(2)
        i = 0
        for j in range(c1):
            nums[i]=0
            i+=1
        for j in range(c2):
            nums[i]=1
            i+=1
        for j in range(c3):
            nums[i]=2
            i+=1
