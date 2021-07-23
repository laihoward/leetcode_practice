class Solution(object):
    def maxProfit(self, prices):
        maxlist=[]
        for i in range(len(prices)):
            maxnum = 0
            for j in range(i,len(prices)):
                if prices[j]-prices[i]>maxnum and prices[j]-prices[i]>0:
                    maxnum = prices[j]-prices[i]
            maxlist.append(maxnum)
        print(max(maxlist))
        return max(maxlist)

#use Dynamic Programming
    def maxProfit(self, prices):
        if not prices:
            return 0
        m = prices[0]
        priceslist = [0]*len(prices)
        for i in range(0,len(prices)):
            priceslist[i] = max(priceslist[i-1],prices[i]-m)
            m=min(prices[i],m)
        return priceslist[-1]