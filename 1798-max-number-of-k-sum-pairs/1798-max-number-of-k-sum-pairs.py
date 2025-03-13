class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        i=0
        j=len(nums)-1
        c=0
        while i<j:
            if nums[i]+nums[j]==k:
                c+=1
                i+=1
                j-=1
            elif nums[i]+nums[j]>k:
                j-=1
            else:
                i+=1
        return c

        