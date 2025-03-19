class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for i in range(k):
            m=min(nums)
            mu=multiplier*m
            l=nums.index(m)
            nums[l]=mu
        return nums
        