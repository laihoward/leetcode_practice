def Count_Inversions(array):
    count =0
    l = []
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]>array[j]:
                count+=1
                y=[array[i]]+[array[j]]
                l.append(y)
    print(l)
    print(count)

# arr = [1, 20, 6, 4, 5]
# arr2 = [8,4,2,1]
# Count_Inversions(arr2)
            
def mergeSort(array):
    count = 0
    if len(array)>1:
        mid = ((len(array)-1)//2)+1
        arrayL = array[:mid]
        arrayR = array[mid:]
        count += mergeSort(arrayL)
        count += mergeSort(arrayR)
        i=j=0
        
        while i<len(arrayL) and j<len(arrayR):
            if arrayL[i]>arrayR[j] :
                count+=1
                j+=1
                if j==len(arrayR):
                  j=0  
                  i+=1
            else:
                j=0
                i+=1
        
    return count
# def mergeSort2(array,start,end):
#     count = 0
#     if start<end:
#         mid=(end+start)//2
#         count +=
arr=[1, 20, 6, 4, 5]
arr2 = [8,4,2,1]
print(mergeSort(arr))
                     

