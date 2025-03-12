class Solution(object):
    def findDisappearedNumbers(self, nums):
        n=len(nums)
        s=set(nums)
        s1=set(i for i in range(1,len(nums)+1))
        return list(s1-s)
        