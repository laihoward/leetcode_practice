class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        count1=0
        count2=0
        newnums=[]
        while count1<len(nums1) and count2<len(nums2):
            if nums1[count1]==nums2[count2]:
                newnums.append(nums1[count1])
                count2+=1
                count1+=1
            elif nums1[count1]>nums2[count2]:
                count2+=1
            else:
                count1+=1
        print(newnums)
        return newnums
s=Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
s.intersect(nums1, nums2)