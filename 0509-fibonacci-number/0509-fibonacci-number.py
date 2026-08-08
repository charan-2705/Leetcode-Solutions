class Solution(object):
    def fib(self, n):
        if n==1:
            return 1
        elif n==2:
            return 1
        else:
            i=2
            n1 = 0
            n2 = 1
            a = 0
            while i<=n:
                a = n1+n2
                n1 = n2
                n2 = a
                i+=1
            return a
        