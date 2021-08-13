class Solution(object):
    def intersection(self, nums1, nums2):
        res1 = set(nums1)
        res2 = set(nums2)
        res=[]
        for i in res2:
            if i in res1:
                res.append(i)
        print(res)
        return res




nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
s=Solution()
s.intersection(nums1,nums2)