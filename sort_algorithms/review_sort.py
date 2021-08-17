def bubble_sort(num):
    for i in range(len(num)):
        for j in range(i,len(num)):
            if num[i]>num[j]:
                num[i],num[j]=num[j],num[i]
    print(num)
    return num
    
array = [38,27,43,3,9,82,10]
bubble_sort(array)