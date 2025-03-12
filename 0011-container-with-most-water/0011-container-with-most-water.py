class Solution(object):
    def maxArea(self, height):
        ma=0
        i=0
        j=len(height)-1
        while i<j:
            w=min(height[i],height[j])
            ma=max(ma,(j-i)*w)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return ma


        