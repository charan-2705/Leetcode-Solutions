class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)
        for i in range(0, length // 2):
            temp1 = s[-(i+1)]
            temp2 = s[i]
            s[-(i+1)] = temp2
            s[i] = temp1
        return s