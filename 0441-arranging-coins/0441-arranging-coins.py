class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        c=0
        while n>=i:
            c+=1
            n-=i
            i+=1
        return c
        