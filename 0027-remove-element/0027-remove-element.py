class Solution(object):
    def removeElement(self, nums, val):
        l=len(nums)
        c=0
        for i in nums:
            if val!=i:
                nums[c]=i
                c+=1
        return c    