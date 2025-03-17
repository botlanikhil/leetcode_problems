class Solution(object):
    def divideArray(self, nums):
        nums.sort()
        for i in nums:
            if nums.count(i)%2!=0:
                return False
        else:
            return True
        
        