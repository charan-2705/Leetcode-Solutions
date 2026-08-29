class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s1=0;s2=0
        for i in nums:
            if i<10 and i>0:
                s1+=i
            elif i>9 and i<100:
                s2+=i
        if s1>s2 or s2>s1:
            return True
        return False


        