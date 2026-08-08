class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sn=len(s);tn=len(t)
        sc=[0]*60
        tc=[0]*60
        for i in range(tn):
            tc[ord(t[i])-65]+=1
        start=0;si=-1;minlen=sn+1
        count=0
        for i in range(sn):
            sc[ord(s[i])-65]+=1
            if sc[ord(s[i])-65]<=tc[ord(s[i])-65]:
                count+=1
            if count==tn:
                while sc[ord(s[start])-65]>tc[ord(s[start])-65] or tc[ord(s[start])-65]==0:
                    if sc[ord(s[start])-65]>tc[ord(s[start])-65]:
                        sc[ord(s[start])-65]-=1
                    start+=1
                clen=i-start+1
                if clen<minlen:
                    minlen=clen
                    si=start
        if si==-1:
            return ""
        return s[si:si+minlen]
