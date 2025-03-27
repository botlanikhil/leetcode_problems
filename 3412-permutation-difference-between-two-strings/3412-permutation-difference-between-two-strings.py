class Solution(object):
    def findPermutationDifference(self, s, t):
        l=list(s)
        l1=list(t)
        s=0
        for i in range(0,len(l)):
            for j in range(0,len(l1)):
                if l[i]==l1[j]:
                    s+=abs(i-j)
        return s