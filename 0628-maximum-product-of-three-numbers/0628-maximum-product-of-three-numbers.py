class Solution(object):
    def maximumProduct(self, nums):
       nums.sort()
       p1 = nums[-3]*nums[-2]*nums[-1]
       p2 = nums[0]*nums[1]*nums[-1]
       return max(p1,p2)
    
