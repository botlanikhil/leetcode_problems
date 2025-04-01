class Solution(object):
    def maxProfit(self, prices, fee):
        buying, selling = 0,-prices[0]
        for i in range(1, len(prices)):
            buying = max(buying, selling + prices[i] - fee)
            selling = max(selling, buying - prices[i])
        return buying