def selectionSort(array):
    for i in range(len(array)-1):
        changeindex = i
        for j in range(i+1,len(array)):
            if array[j]<array[changeindex]:
                changeindex=j
        array[changeindex],array[i] = array[i],array[changeindex]
        

def recur_selectionSort(array,start,end):
    changeindex = start
    for j in range(changeindex+1,end):
        if array[j]<array[changeindex]:
            changeindex=j
    array[start],array[changeindex] = array[changeindex],array[start]
    if start+1<end:
        recur_selectionSort(array,start+1,end)





array = [38,27,43,3,9,82,10]
a2=[40, 76, 41, 57, 31, 52, 91, 23, 26, 63]
selectionSort(a2)
print(a2)