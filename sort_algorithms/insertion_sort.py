def insertionSort(array):
    for i in range(len(array)):
        j = i-1
        key =  array[i]
        while j>-1 and key<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1] = key
    


if __name__ == '__main__':
    array = [38,27,43,3,9,82,10]
    insertionSort(array)
    print(array)
