class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for i in range(len(nums) - k):
            window_sum += nums[i + k] - nums[i]  # Slide the window
            max_sum = max(max_sum, window_sum)  
        
        return round(max_sum,2) / k