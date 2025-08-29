class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        maxi=0
        d=0
        for i,j in dimensions:
            d1=math.sqrt(i*i+j*j)
            if d1>d:
                d=d1
                maxi=(i*j)
            elif d==d1:
                maxi=max(maxi,i*j)

        return maxi
            