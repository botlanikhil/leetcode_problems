class Solution(object):
    def maxProfit(self, prices):
        price=float('inf')
        maxi=0
        for i in prices:
            if i<price:
                price=i
            maxi=max(maxi,i-price)
        return maxi