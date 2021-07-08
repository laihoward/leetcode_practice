import random
def createRandom(start,end): #製作一個start到end之間的隨機數
    t = (start+random.randint(0,100)%(end-start+1))
    
    return t

def randomizedBS(array,start,end,x):
    if end>=1:
        midindex = createRandom(start,end)
        if array[midindex] == x:
            return midindex
        if array[midindex]>x:
            return randomizedBS(array,start,midindex-1,x)
        elif array[midindex]<x:
            return randomizedBS(array,midindex+1,end,x)
    return -1

array = [2, 3, 4, 10, 40]
finalindex = randomizedBS(array,0,len(array)-1,40)
if finalindex==-1:
    print('Element is not present in array' )
else:
    print('Element is present at index',finalindex)