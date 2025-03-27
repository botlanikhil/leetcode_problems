class Solution(object):
    def scoreOfString(self, s):
        s1=0
        for i in range(0,len(s)-1):
            d=ord(s[i])-ord(s[i+1])
            s1+=abs(d)

        return s1
        