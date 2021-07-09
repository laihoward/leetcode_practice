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

arr = [1, 20, 6, 4, 5]
arr2 = [8,4,2,1]
Count_Inversions(arr2)
            
