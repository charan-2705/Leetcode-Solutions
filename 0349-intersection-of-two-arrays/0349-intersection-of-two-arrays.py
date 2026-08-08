class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        for i in nums1:
            if i in nums2:
                l.append(i)
        myset=set()
        for i in l:
            if i not in myset:
                myset.add(i)
        return list(myset)
            


        