class Solution(object):
    #Will Time Limit Exceeded
    def maxProfit(self, prices):
        maxnum = 0
        for i in range(len(prices)):

            for j in range(i,len(prices)):
                if prices[j]-prices[i]>maxnum and prices[j]-prices[i]>0:
                    maxnum = prices[j]-prices[i]
        return maxnum

#use Dynamic Programming
    def maxProfit2(self, prices):
        if not prices:
            return 0
        m = prices[0]
        priceslist = [0]*len(prices)
        for i in range(0,len(prices)):
            priceslist[i] = max(priceslist[i-1],prices[i]-m)
            m=min(prices[i],m)
        return priceslist[-1]

prices = [7,1,5,3,6,4]
s=Solution()
print(s.maxProfit(prices))