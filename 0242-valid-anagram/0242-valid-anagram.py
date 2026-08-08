class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sn=len(s);tn=len(t)
        sc=[0]*26
        tc=[0]*26
        if sn!=tn:
            False
        for i in range(sn):
            sc[ord(s[i])-97]+=1
        for i in range(tn):
            tc[ord(t[i])-97]+=1
        return sc==tc
        