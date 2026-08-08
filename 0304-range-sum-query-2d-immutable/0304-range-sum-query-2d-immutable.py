class NumMatrix(object):

    def __init__(self, matrix):
        r=len(matrix)
        c=len(matrix[0])
        self.prefix=[[0]*(c+1) for j in range(r+1)]
        for i in range(1,r+1):
            sum=0
            for j in range(1,c+1):
                sum+=matrix[i-1][j-1]
                self.prefix[i][j]=sum+self.prefix[i-1][j]
        

    def sumRegion(self, r1, c1, r2, c2):
        br=self.prefix[r2+1][c2+1]
        above=self.prefix[r1][c2+1]
        left=self.prefix[r2+1][c1]
        cr=self.prefix[r1][c1]
        return br-above-left+cr


