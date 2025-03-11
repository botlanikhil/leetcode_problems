class Solution(object):
    def mergeAlternately(self, word1, word2):
        l3=[]
        for i,j in zip(word1,word2):
            l3.append(i+j)
        l3.append(word1[len(word2):])
        l3.append(word2[len(word1):])
        return "".join(l3)