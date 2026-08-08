class Solution(object):
    def isPerfectSquare(self, num):
        n = int(sqrt(num))
        if n*n == num :
            return True
        else:
            return False

        