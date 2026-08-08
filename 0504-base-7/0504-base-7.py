class Solution(object):
    def convertToBase7(self, n):
        s =""
        x = abs(n)
        while x!=0:
            a = x%7
            s = str(a)+s
            x = x//7
        if n ==0:
            return "0"
        if n<0:
            s="-"+s
            return s
        return s