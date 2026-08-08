class Solution(object):
    def findDiagonalOrder(self, mat):
        m=len(mat);n=len(mat[0]);dir=True
        r=0;c=0;res=[]
        while r<m and c<n:
            if dir:
                while r>0 and c<n-1:
                    res.append(mat[r][c])
                    r=r-1
                    c=c+1
                res.append(mat[r][c])
                if c==n-1:
                    r+=1
                else:
                    c+=1
            else:
                while r<m-1 and c>0:
                    res.append(mat[r][c])
                    r=r+1
                    c=c-1
                res.append(mat[r][c])
                if r==m-1:
                    c+=1
                else:
                    r+=1
            dir = not dir
        return res