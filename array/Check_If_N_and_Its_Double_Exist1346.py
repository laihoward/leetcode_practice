class Solution(object):
    def checkIfExist(self, arr):
        x =False
        i=0
        for i in range(len(arr)):
            if x ==False:
                j = 0
                for j in range(len(arr)):
                    if arr[i] != arr[j]*2:
                        x = False
                    elif arr[i] == 0 and arr[j] == 0   :
                        if i != j :
                            x = True
                            break
                        else:           
                            x = False
                    else: 
                        x = True
                        break
        print(x)
        return x
                    
      
def main():
    s=Solution()
    array = [-2,0,10,-19,4,6,-8]
    array2 = [7,1,14,11]
    array3 =[3,1,7,11]
    array4 =[0,0]
    s.checkIfExist(array)
    s.checkIfExist(array2)
    s.checkIfExist(array3)
    s.checkIfExist(array4)
if __name__ == '__main__':
    main()