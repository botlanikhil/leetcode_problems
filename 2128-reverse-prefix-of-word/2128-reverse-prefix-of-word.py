class Solution(object):
    def reversePrefix(self, word, ch):
        s=''
        if ch in word:
            a=word.index(ch)
            s+="".join(reversed(word[0:a+1]))
            s=s+word[a+1:len(word)]
            return s

        else:
            return word