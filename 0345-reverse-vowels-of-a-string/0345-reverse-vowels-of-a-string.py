class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        st="aeiouAEIOU"
        l=0
        r=len(s)-1
        while l<r:
            while l<r and s[l] not in st:
                l+=1
                continue
            while l<r and s[r] not in st:
                r=r-1
                continue
            s[l],s[r]=s[r],s[l]
            l=l+1
            r=r-1
        s=''.join(s)
        return s