class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def solve(n):
            x = n
            while x!=0:
                a = x%10
                if a==0:
                    return False
                if n%a!=0:
                    return False
                x = x//10
            return True
        res=[]
        for i in range(left,right+1):
            if solve(i):
                res.append(i)
        return res

        