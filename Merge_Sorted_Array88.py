class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i=m-1
        j=n-1
        k = n+m-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
                k-=1
            else:
                nums1[k]=nums2[j]
                j-=1
                k-=1
        while i>=0:
            nums1[k]=nums1[i]
            i-=1
            k-=1

        while j>=0: 
            nums1[k]=nums2[j]
            j-=1
            k-=1
        print(nums1)
        return nums1
def main():
    s=Solution()
    array = [1,2,3,0,0,0]
    array2 =  [2,5,6]
    m = 3
    n = 3
    s.merge(array,m,array2,n)
if __name__ == '__main__':
    main()
