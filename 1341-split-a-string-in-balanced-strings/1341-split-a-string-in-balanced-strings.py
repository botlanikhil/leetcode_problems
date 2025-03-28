class Solution(object):
    def balancedStringSplit(self, s):
        cnt_r = 0
        cnt_s = 0
        k = 0
        for i in range(len(s)):
            if s[i] == 'R':
                cnt_r += 1
            else:
                cnt_s += 1
            if cnt_r == cnt_s:
                k += 1
        return k

        