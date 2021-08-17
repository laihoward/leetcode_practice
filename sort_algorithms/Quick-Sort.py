array = [38,27,43,3,9,82,10]
array2 = [38,27,43,3,9,82,10,15]


def partition(array,start,end):
    low = start -1
    pivot = array[end]
    for high in range(start, end):
        if array[high]<pivot:
            low +=1
            array[low],array[high] =array[high],array[low]
            high +=1
        else:
            high +=1
    low+=1
    array[low],array[high] =array[high],array[low]
    print(array)
    return low 

def quickSort(array,low,high):
    if len(array) == 1:
        return array
    if low < high:
        pivotposition = partition(array, low, high)
        quickSort(array, low, pivotposition-1)
        quickSort(array, pivotposition+1, high)
    
    
if __name__ == '__main__':
    array = [38,27,43,3,9,82,10]
    
    quickSort(array, 0, len(array)-1)
    print(array)
   
