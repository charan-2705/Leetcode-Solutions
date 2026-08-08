class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif 1 + (num - 1) % 9 == 0:
            return 9
        else:
            return 1 + (num - 1) % 9