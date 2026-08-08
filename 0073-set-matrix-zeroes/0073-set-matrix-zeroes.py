class Solution(object):
    def setZeroes(self, mat):
        m=len(mat)
        n=len(mat[0])
        flag=1
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    mat[i][0]=0
                    if j==0:
                        flag=0
                    else:
                        mat[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if mat[0][j]==0 or mat[i][0]==0:
                    mat[i][j]=0
        if mat[0][0]==0:
            for j in range(1,n):
                mat[0][j]=0
        if flag==0:
            for i in range(m):
                mat[i][0]=0