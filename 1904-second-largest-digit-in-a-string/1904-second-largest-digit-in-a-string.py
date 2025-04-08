class Solution(object):
    def secondHighest(self, s):
        digits=set()
        for ch in s:
            if ch.isdigit():
                digits.add(int(ch))
        sorted_digits = sorted(digits)
        if len(sorted_digits) >= 2:
            return sorted_digits[-2]  
        else:
            return -1