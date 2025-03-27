class Solution(object):
    def defangIPaddr(self, address):
        p=list(address)
        s=''
        for i in range(0,len(p)):
            if p[i]==".":
                p[i]="[.]"
        s=''.join(p)
        return s
        