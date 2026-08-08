class Solution(object):
    def subsets(self, nums):
        res = []
        def allsubsets(ans,index):
            if index==len(nums):
                res.append(ans[:])
                return 
            
            ans.append(nums[index])
            allsubsets(ans,index+1)
            ans.pop()
            allsubsets(ans,index+1)

        allsubsets([],0)
        return res
        