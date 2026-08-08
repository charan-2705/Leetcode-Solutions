class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        hashmap={}
        k = 0
        for i, string in enumerate(t):
            if string in hashmap:
                hashmap[string].append(i)
            else:
                hashmap[string]=[i]
        for string in s:
            if string not in hashmap.keys(): return False
            found = False
            for i in hashmap[string]:
                if i >= k:
                    k = i + 1
                    found = True
                    break
            if not found:
                return False
        
        return True