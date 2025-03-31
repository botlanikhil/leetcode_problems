class Solution(object):
    def reverseOnlyLetters(self, s):
        l=list(s)
        i=0
        j=len(l)-1
        while i < j:
            if l[i].isalpha() and l[j].isalpha():
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
            elif not l[i].isalpha():
                i += 1
            else:
                j -= 1
        return "".join(l)
        