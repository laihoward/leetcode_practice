class Solution(object):
    def replaceElements(self, arr):
        j=0
        if len(arr) == 1:
            arr[0]=-1
        else:
            for j in range(len(arr)-1):
                print("j",j)
                if j == len(arr)-2:
                    maxnum = arr[j+1]
                    print(maxnum)
                    for i in arr[j+1:]:
                        if i>maxnum:
                            maxnum = i
                    arr[j] = maxnum
                    arr[j+1] = -1
                else:
                    maxnum = arr[j+1]
                    print(maxnum)
                    for i in arr[j+1:]:
                        if i>maxnum:
                            maxnum = i
                    arr[j] = maxnum      
                    print(maxnum)
                    print("==========")
        print(arr)
        return arr
                    
      
def main():
    s=Solution()
    array = [17,18,5,4,6,1]
    array2 = [400]
    array3 =[0,3,2,1]
    array4 =[0,1,2,3,4,5,6,7,8,9]
    s.replaceElements(array)
    s.replaceElements(array2)
    # s.replaceElements(array3)
    # s.replaceElements(array4)
if __name__ == '__main__':
    main()