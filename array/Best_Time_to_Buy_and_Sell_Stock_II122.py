class Solution(object):
    def maxProfit(self, prices):
        sumprices = 0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                sumprices+=prices[i+1]-prices[i]
        print(sumprices)
        return sumprices