class Solution(object):
    def searchInsert(self, nums, target):
        i=1
        n=len(nums)
        if target<=nums[0]:
            return 0
        else:
            while i<n:
                if nums[i-1]<target<=nums[i]:
                    return i
                i+=1
            
            return n
            

        