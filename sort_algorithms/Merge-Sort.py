
def mergesort(array):
    # divides the input array into two halves
    if len(array) >1:
        r=len(array)
        middle  = 1+ (r-1)//2
        L_array = array[:middle]
        R_array = array[middle:]
        mergesort(L_array)
        mergesort(R_array)
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
        print(array)


if __name__ == '__main__':
    array = [38,27,43,3,9,82,10]
    mergesort(array)
