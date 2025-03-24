class Solution(object):
    def maxProfit(self, prices):
        price=float('inf')
        maxprofit=0
        for i in prices:
            if i < price:
                price=i
            else:
                maxprofit=max(maxprofit,i-price) 
        return maxprofit