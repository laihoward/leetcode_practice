class sortAlgorithms(object):
    def partition(self,array,start,end):
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
        return low 

    def quickSort(self,array,low,high):
        if len(array) == 1:
            return array
        if low < high:
            pivotposition = self.partition(array, low, high)
            self.quickSort(array, low, pivotposition-1)
            self.quickSort(array, pivotposition+1, high)

    def mergesort(self,array):
        # divides the input array into two halves
        if len(array) >1:
            r=len(array)
            middle  = 1+ (r-1)//2
            L_array = array[:middle]
            R_array = array[middle:]
            self.mergesort(L_array)
            self.mergesort(R_array)
            i = j = k = 0

            while i < len(L_array) and j < len(R_array):
                    if L_array[i] < R_array[j]:
                        array[k] = L_array[i]
                        i += 1
                    else:
                        array[k] = R_array[j]
                        j += 1
                    k += 1
        
            # Checking if any element was left
            while i < len(L_array):
                array[k] = L_array[i]
                i += 1
                k += 1

            while j < len(R_array):
                array[k] = R_array[j]
                j += 1
                k += 1    
    
    def insertionSort(self,array):
        for i in range(len(array)):
            j = i-1
            key =  array[i]
            while j>-1 and key<array[j]:
                array[j+1]=array[j]
                j-=1
            array[j+1] = key
        
    def selectionSort(self,array):
        for i in range(len(array)-1):
            changeindex = i
            for j in range(i+1,len(array)):
                if array[j]<array[changeindex]:
                    changeindex=j
            array[changeindex],array[i] = array[i],array[changeindex]
            
    def recur_selectionSort(self,array,start,end):
        changeindex = start
        for j in range(changeindex+1,end):
            if array[j]<array[changeindex]:
                changeindex=j
        array[start],array[changeindex] = array[changeindex],array[start]
        if start+1<end:
            self.recur_selectionSort(array,start+1,end)

    def heapify(self,array, n, i):
        largestindex = i
        indexL = 2*i+1
        indexR = 2*i+2
        if indexL<n and array[i]<array[indexL]:
            largestindex=indexL
        if indexR<n and array[largestindex]<array[indexR]:
            largestindex=indexR
        if largestindex!=i:
            array[i],array[largestindex]=array[largestindex],array[i]
            self.heapify(array,n,largestindex)

    def heapSort(self,array):
        n = len(array)
        # Build a maxheap.
        #最後一個parent root的index
        for i in range(n//2-1,-1,-1):
            self.heapify(array,n,i)
    
        for i in range(n-1,0,-1):
            array[0],array[i]=array[i],array[0]
            self.heapify(array,i,0)

if __name__ == '__main__':
    array = [38,27,43,3,9,82,10]
    s = sortAlgorithms()
    # s.quickSort(array, 0, len(array)-1)
    # s.mergesort(array)
    # s.insertionSort(array)
    # s.selectionSort(array)
    # s.recur_selectionSort(array, 0, len(array))
    s.heapSort(array)
    print(array)