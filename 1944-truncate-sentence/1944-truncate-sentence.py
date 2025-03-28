class Solution(object):
    def truncateSentence(self, s, k):
        s=s.split()
        new=''
        for i in range(k):
            new+=s[i]+' '
        new=new.strip()
        return new