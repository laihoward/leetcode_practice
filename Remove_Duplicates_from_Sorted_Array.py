class Solution(object):
    def removeDuplicates(self, nums):
        count =0
        i = 0
        while i < len(nums)-1:
            if nums[i]==nums[i+1]:
                nums.pop(i+1)
                i-=1
            i+=1
        count =  len(nums)
        print(nums)
        print(count)
        return count



def main():
    s=Solution()
    array = [1,1,2]
    array2 = [0,0,1,1,1,2,2,3,3,4]
    s.removeDuplicates(array)
    s.removeDuplicates(array2)
if __name__ == '__main__':
    main()