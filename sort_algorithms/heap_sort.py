def heapify(array, n, i):
    largestindex = i
    indexL = 2*i+1
    indexR = 2*i+2
    if indexL<n and array[i]<array[indexL]:
        largestindex=indexL
    if indexR<n and array[largestindex]<array[indexR]:
        largestindex=indexR
    if largestindex!=i:
        array[i],array[largestindex]=array[largestindex],array[i]
        heapify(array,n,largestindex)



def heapSort(array):
    n = len(array)
    # Build a maxheap.
    #最後一個parent root的index
    for i in range(n//2-1,-1,-1):
        heapify(array,n,i)
    
    for i in range(n-1,0,-1):
        array[0],array[i]=array[i],array[0]
        heapify(array,i,0)



