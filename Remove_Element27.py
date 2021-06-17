

class Solution(object):
    def removeElement(self, nums, val):
        count =0
        for i in nums:
            if i != val:
                nums[count] = i
                count += 1
        print(nums)
        return count



def main():
    s=Solution()
    array = [3,2,2,3]
    val1 = 3
    array2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    s.removeElement(array,val1)
    # s.removeElement(array2,val2)
if __name__ == '__main__':
    main()