class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count = 0
        for num in range(low, high + 1):
            s = str(num)
            length = len(s)
            if length % 2 == 0:
                half = length // 2
                left_sum = sum(int(d) for d in s[:half])
                right_sum = sum(int(d) for d in s[half:])
                if left_sum == right_sum:
                    count += 1
        return count
        