class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        l1 = nums[-1]*nums[-2]*nums[-3]
        l2 = nums[0]*nums[1]*nums[-1]
        return max(l1,l2)

        