class Solution(object):
    def findPeakElement(self, nums):
        n=len(nums)
        l=0
        h=n-1
        while (l<h):
            mid=(l+h)//2
            if (nums[mid] < nums[mid+1]):   
                l=mid+1
            else:
                h=mid
        return l
        