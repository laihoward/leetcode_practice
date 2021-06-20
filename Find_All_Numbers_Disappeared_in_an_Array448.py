class Solution(object):
    def findDisappearedNumbers(self, arr):
        finalarr = []
        numset = set(arr)
        for num in range(1, len(arr) + 1):
            if num not in numset:
                finalarr.append(num)
        print(finalarr)
        return finalarr
                    
      
def main():
    s=Solution()
    array = [4,3,2,7,8,2,3,1]
    array2 = [1,1]
    s.findDisappearedNumbers(array)
    s.findDisappearedNumbers(array2)

if __name__ == '__main__':
    main()