def bubble_sort(num):
    for i in range(len(num)):
        for j in range(len(num)-i-1):
            if num[j]>num[j+1]:
                num[j+1],num[j]=num[j],num[j+1]
    print(num)
    return num



def selection_sort(num):
    len_num=len(num)
    
    for i in range(len_num):
        res = i
        for j in range(i,len_num-1):
            if num[res]>num[j+1]:
                res = j+1
        # print(num[res])
        num[i],num[res]=num[res],num[i]
    print(num)
    return num




    
array = [38,27,43,3,9,82,10]
# bubble_sort(array)
selection_sort(array)