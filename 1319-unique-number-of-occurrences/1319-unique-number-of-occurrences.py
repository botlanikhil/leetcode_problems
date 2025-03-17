class Solution(object):
    def uniqueOccurrences(self, arr):
        d={}
        l=[]
        for i in arr:
            k=i
            v=arr.count(i)
            d.update({k:v})
        for j in d:
            if d[j]  in l:
                return False
            l.append(d[j])
        return True
        