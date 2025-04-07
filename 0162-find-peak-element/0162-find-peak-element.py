class Solution(object):
    def findPeakElement(self, nums):
        t=0  
        maxi=max(nums)
        for i in range(0,len(nums)):
            if maxi==nums[i]:
                t=i
        return t 
        