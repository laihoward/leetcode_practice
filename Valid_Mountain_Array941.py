class Solution(object):
    def validMountainArray(self, arr):
        x =True
        i=0
        maxnum = arr[i]
        maxindex = i
        for i in range(len(arr)-1):
            if arr[i+1]>arr[i]:
                maxnum = arr[i+1]
                maxindex = i+1
        j=0
        if maxindex==0:
            x =False
        elif maxindex==len(arr)-1:
            x =False
        else:
            for j in range(maxindex):
                # print(arr[j])
                if arr[j]>=arr[j+1]:
                    x =False 
                    break
        # print(maxindex)
            k = 0
            for k in range(len(arr)-maxindex-1):
                # print(arr[k+maxindex])
                if arr[k+maxindex]<=arr[k+maxindex+1]:
                    x =False 
                    break
        print(x)
        return x
                    
      
def main():
    s=Solution()
    array = [2,1]
    array2 = [3,5,5]
    array3 =[0,3,2,1]
    array4 =[0,1,2,3,4,5,6,7,8,9]
    s.validMountainArray(array)
    s.validMountainArray(array2)
    s.validMountainArray(array3)
    s.validMountainArray(array4)
if __name__ == '__main__':
    main()