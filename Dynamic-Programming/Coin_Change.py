
#use Bottom up
#https://www.youtube.com/watch?v=6igPE6zlvCY&ab_channel=Michelle%E5%B0%8F%E6%A2%A6%E6%83%B3%E5%AE%B6
class Solution(object):
    def coinChange(self, coins, amount):
        
        dp=[0]+[-1]*amount
        for i in range(amount):
            if dp[i]<0:
                continue
            for j in coins:
                if i+j>amount:
                    continue
                if dp[i+j]<0 or dp[i+j]>dp[i]+1:
                    dp[i+j]=dp[i]+1
                print(dp)
        print(dp)
        return dp[amount]
  

# coins = [186,419,83,408]
# amount = 6249
coins = [1,2,5]
amount = 11
s=Solution()
print(s.coinChange(coins,amount))