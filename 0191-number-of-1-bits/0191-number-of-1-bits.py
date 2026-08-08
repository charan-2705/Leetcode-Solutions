class Solution:
    def hammingWeight(self, n: int) -> int:
        x = str(bin(n))
        c = 0
        for i in range(len(x)):
            if x[i]=='1':
                c+=1
        return c


        