class Solution(object):
    def trap(self, h):
        n=len(h)
        left=[0]*n;right=[0]*n;water=0
        left[0]=h[0];right[n-1]=h[n-1]
        for i in range(n):
            left[i]=max(h[i],left[i-1])
        for i in range(n-2,-1,-1):
            right[i]=max(h[i],right[i+1])
        for i in range(n):
            water+=(min(left[i],right[i])-h[i])
        return water
        
        