class Solution(object):
    def isPalindrome(self, x):
        if x <0:
            return False
        num = x
        rev = 0
        while x!=0:
            a = x%10
            rev = rev*10+a
            x = x//10
        if num == rev:
            return True
        else:
            return False
        