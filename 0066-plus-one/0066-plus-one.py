class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        num = 0
        for i in range(len(nums)):
            num = num*10 + nums[i]
        num+=1
        l=[]
        while(num):
            l.append(num%10)
            num=num//10
        x = l[::-1]
        return x
        