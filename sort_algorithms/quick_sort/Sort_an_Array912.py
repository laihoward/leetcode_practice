
def partition(start, end, array):
    pivotIndex = start
    pivot =array[pivotIndex]
    while start<end:

        while start<len(array) and array[start]<=pivot:
            start+=1
        while array[end]>pivot:
            end-=1
        
        if (start<end):
            array[start],array[end]=array[end],array[start]
    array[end],array[pivotIndex] = array[pivotIndex],array[end]
    return end


def quick_sort(start, end, array):
    if (start<end):
        p = partition(start,end,array)
        quick_sort(start,p-1,array)
        quick_sort(p+1,end,array)
    


array = [ 10, 7, 8, 9, 1, 5 ]
quick_sort(0, len(array) - 1, array)
print(array)
