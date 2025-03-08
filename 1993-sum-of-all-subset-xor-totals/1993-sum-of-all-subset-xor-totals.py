class Solution(object):
    def subsetXORSum(self, nums):
        xor_sum = 0
        for num in nums:
            xor_sum |= num  
        return xor_sum * (1 << (len(nums) - 1))
        