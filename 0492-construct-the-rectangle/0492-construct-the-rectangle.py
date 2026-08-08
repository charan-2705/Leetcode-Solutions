class Solution(object):
    def constructRectangle(self, area):
        l=[]
        for i in range(1,area+1):
            if area%i == 0:
                a = i
                b = area//i
                if a>=b:
                    l.append(a)
                    l.append(b)
                    return l
        return l