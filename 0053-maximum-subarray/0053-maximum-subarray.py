class Solution(object):
    def maxSubArray(self, nums):
        c=0
        j=nums[0]
        for i in nums:
            if c<0:
                c=0
            c+=i
            j=max(j,c)
        return j
        