class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        word="".join(word1)
        word3="".join(word2)
        if word==word3:
            return True
        else:
            return False
        