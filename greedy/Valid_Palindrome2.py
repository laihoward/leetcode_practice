class Solution(object):
    def validPalindrome(self, s):
        l=0
        r=len(s)-1
        while l<=r :
            if s[l]==s[r]:
                l+=1
                r-=1           
            else:
                del_l=s[l+1:r+1]
                del_r=s[l:r]
                if del_l == del_l[::-1] or del_r==del_r[::-1]:
                    return True
                else:
                    return False
        return True
        



s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    
sol=Solution()
print(sol.validPalindrome(s))