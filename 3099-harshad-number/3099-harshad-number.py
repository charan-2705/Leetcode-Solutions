class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n = x;s=0
        while n!=0:
            a = n%10
            s+=a
            n =  n//10
        if x%s==0:
            return s
        return -1

        