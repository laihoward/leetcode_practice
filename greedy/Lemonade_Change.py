class Solution(object):
    def lemonadeChange(self, bills):
        change_5 = 0
        change_10=0
        for i in bills:
            if i==5:
                change_5+=1
            elif i==10 :
                if change_5>=1:
                    change_5-=1
                    change_10+=1
                else:
                    return False
            else:
                if change_10 and change_5:
                    change_5-=1
                    change_10-=1
                elif change_5>=3:
                    change_5-=3
                else:
                    return False
        return True



bills = [10,10]
s=Solution()
print(s.lemonadeChange(bills))