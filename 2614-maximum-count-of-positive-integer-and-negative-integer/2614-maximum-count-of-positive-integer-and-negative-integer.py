class Solution(object):
    def maximumCount(self, nums):
        c=0
        c1=0
        for i in nums:
            if i>0:
                c+=1
            if i<0:
                c1+=1
        return max(c,c1)
        