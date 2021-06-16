
# class Solution(object):
#     def sortedSquares(self, nums):
#         nums= [number ** 2 for number in nums]
#         for i in range(len(nums)):
#             for j in range(len(nums)-1-i):
#                 if nums[j]>nums[j+1]:
#                     swapnum = nums[j]
#                     nums[j] =nums[j+1]
#                     nums[j+1] = swapnum
#         print(nums)
#         return nums
class Solution:
    #nums為List[int]型態 return為List[int]型態
    def sortedSquares(self, nums: 'List[int]') -> 'List[int]':
        newnums = []
        for i in nums:
            newnums.append(i**2)
        newnums.sort()
        print(newnums)
        return newnums

def main():
    s=Solution()
    array = [-4,-1,0,3,10]
    array2 =  [-7,-3,2,3,11]
    s.sortedSquares(array)
    s.sortedSquares(array2)
if __name__ == '__main__':
    main()

