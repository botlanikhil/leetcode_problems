class Solution(object):
    def getLucky(self, s, k):
        res = ''
        for c in s: 
            res += str(ord(c) - ord('a') + 1)
        for i in range(k): 
            res = str(sum([int(c) for c in res]))
        return int(res)
        