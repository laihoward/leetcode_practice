class Solution(object):
    def isPalindrome(self, s):
        slist = []
        for i in s:
            if i.isalnum():
                slist.append(i.lower())
        l = len(slist)
        print(l//2)
        for i in range(0,l//2):
            if slist[i]!=slist[l-1-i]:
                return False
        return True

    def isPalindrome(self, s):
        i = -1
        j = len(s)
        while True:
            i += 1
            j -= 1
            if i > j:
                return True
            while i < j:
                if not s[i].isalnum():
                    i += 1
                else:
                    break
            while i < j:
                if not s[j].isalnum():
                    j -= 1
                else:
                    break
            if s[i].lower() != s[j].lower():
                return False

string = "A man, a plan, a canal: Panama"
s=Solution()
print(s.isPalindrome(string))